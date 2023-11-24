import uuid

from transformers import FlaxAutoModelForSeq2SeqLM
from transformers import AutoTokenizer

from server.data.models.recipe import Recipe


class HuggingFace(object):
    _MODEL_NAME_OR_PATH = "flax-community/t5-recipe-generation"
    _tokenizer = AutoTokenizer.from_pretrained(_MODEL_NAME_OR_PATH, use_fast=True)
    _model = FlaxAutoModelForSeq2SeqLM.from_pretrained(_MODEL_NAME_OR_PATH)

    _prefix = "items: "

    _generation_kwargs = {
        "max_length": 512,
        "min_length": 64,
        "no_repeat_ngram_size": 3,
        "do_sample": True,
        "top_k": 60,
        "top_p": 0.95
    }

    _tokens_map = {
        "<sep>": "--",
        "<section>": "\n"
    }

    @classmethod
    def generate(cls, ingredients):
        return cls.__parse_recipe(cls.__generation_function(ingredients))

    @staticmethod
    def __skip_special_tokens(text, special_tokens):
        for token in special_tokens:
            text = text.replace(token, "")

        return text

    @classmethod
    def __target_postprocessing(cls, texts, special_tokens):
        if not isinstance(texts, list):
            texts = [texts]

        new_texts = []
        for text in texts:
            text = cls.__skip_special_tokens(text, special_tokens)

            for k, v in cls._tokens_map.items():
                text = text.replace(k, v)

            new_texts.append(text)

        return new_texts

    @classmethod
    def __generation_function(cls, texts):
        _inputs = texts if isinstance(texts, list) else [texts]
        inputs = [cls._prefix + inp for inp in _inputs]
        inputs = cls._tokenizer(
            inputs,
            max_length=256,
            padding="max_length",
            truncation=True,
            return_tensors="jax"
        )

        input_ids = inputs.input_ids
        attention_mask = inputs.attention_mask

        output_ids = cls._model.generate(
            input_ids=input_ids,
            attention_mask=attention_mask,
            **cls._generation_kwargs
        )
        generated = output_ids.sequences
        generated_recipe = cls.__target_postprocessing(
            cls._tokenizer.batch_decode(generated, skip_special_tokens=False),
            cls._tokenizer.all_special_tokens
        )
        return generated_recipe

    @staticmethod
    def __parse_recipe(generated):
        recipes = []

        for text in generated:
            sections = text.split("\n")
            recipe = Recipe(uuid.uuid4().__str__())

            for section in sections:
                section = section.strip()

                if section.startswith("title:"):
                    section = section.replace("title:", "")
                    recipe.title = f"{section.strip().capitalize()}"
                elif section.startswith("ingredients:"):
                    section = section.replace("ingredients:", "")
                    ingredients = [f"{info.strip().capitalize()}" for i, info in enumerate(section.split("--"))]
                    recipe.ingredients = ingredients
                elif section.startswith("directions:"):
                    section = section.replace("directions:", "")
                    directions = [f"{info.strip().capitalize()}" for i, info in enumerate(section.split("--"))]
                    recipe.directions = directions

            recipes.append(recipe)

        return recipes
