from server.data.repositories.recipe_repository import RecipeRepository

recipe_repository = RecipeRepository()


def get_recipe(recipe_id, title):  # noqa: E501
    """searches for existing recipes and lists them

    By passing in the appropriate options, you can search for available recipes in the system  # noqa: E501
 
    :param recipe_id: ID of the recipe to be retrieved
    :param title: Title of the recipe to be retrieved

    :rtype: List[Recipe]
    """
    return recipe_repository.get_recipe(recipe_id, title)
