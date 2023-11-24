import connexion

from server.data.models.recipe import Recipe  # noqa: E501
from server.data.repositories.recipe_repository import RecipeRepository
from server.huggingface.hugging_face import HuggingFace

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


def delete_recipe(recipe_id):  # noqa: E501
    """Delete an existing recipe from the system

    Deletes an existing recipe from the system using id # noqa: E501

    :param recipe_id: Recipe id to be deleted
    :type recipe_id: str

    :rtype: None
    """
    return 'do some magic!'


def search_recipes(search_string=None, skip=None, limit=None):  # noqa: E501
    """searches for existing recipes and lists them

    By passing in the appropriate options, you can search for available recipes in the system  # noqa: E501

    :param search_string: pass an optional search string for looking up recipes
    :type search_string: str
    :param skip: number of records to skip for pagination
    :type skip: int
    :param limit: maximum number of records to return
    :type limit: int

    :rtype: List[Recipe]
    """
    return 'do some magic!'


def update_recipe(body=None):  # noqa: E501
    """Modify a recipe and save it back to the system

    Loads an existing recipe, change it and save it back in the system # noqa: E501

    :param body: Updated recipe body
    :type body: dict | bytes

    :rtype: Recipe
    """
    if connexion.request.is_json:
        body = Recipe.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
