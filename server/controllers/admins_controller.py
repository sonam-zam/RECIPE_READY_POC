import json

import connexion

from server.data.models.recipe import Recipe  # noqa: E501
from server.data.repositories.recipe_repository import RecipeRepository
from server.huggingface.hugging_face import HuggingFace
from server.util import deserialize_model

recipe_repository = RecipeRepository()


def add_recipe(body=None):  # noqa: E501
    """Generates a recipe and adds it to the system

    Generate a recipe using HuggingFace and add it to the system # noqa: E501

    :param body: Ingredients to generate recipe from
    :type body: List[]

    :rtype: Recipe
    """
    recipes = []
    for recipe in HuggingFace.generate(body):
        result = recipe_repository.insert_recipe(recipe)
        recipes.append(result)

    return recipes


def delete_recipe(recipe_id, title):  # noqa: E501
    """Delete an existing recipe from the system

    Deletes an existing recipe from the system using id # noqa: E501

    :param recipe_id: Recipe id to be deleted
    :param title: Title of the recipe to be deleted
    :type recipe_id: str

    :rtype: None
    """
    return recipe_repository.delete_recipe(recipe_id, title)


def update_recipe(body=None):  # noqa: E501
    """Modify a recipe and save it back to the system

    Loads an existing recipe, change it and save it back in the system # noqa: E501

    :param body: Updated recipe body
    :type body: dict | bytes

    :rtype: Recipe
    """
    return recipe_repository.update_recipe(Recipe.from_dict(body))


def get_all_recipes():
    """Get all the saved recipes from the system

    :return: List of recipes
    """
    return recipe_repository.get_all_recipes()


def search_recipe(query_string):  # noqa: E501
    """searches for existing recipes and lists them

    By passing in a keyword, you can search for available recipes in the system  # noqa: E501

    :param query_string: Keyword to scan for

    :rtype: List[Recipe]
    """
    return recipe_repository.search_recipe(query_string)
