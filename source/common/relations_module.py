def get_relation_by_model(model: str) -> dict:
    """
    :param model: Model name
    :return: Dictionary with relationships
    """
    switcher = {
        'user': get_relations_for_user(),
        'todo': get_relations_for_todo()
    }

    return switcher.get(model)


def get_relations_for_user() -> dict:
    """
    :return: Dictionary with user relationships
    """
    return {
        'todo': {
            'localField': '_id',
            'foreignField': 'user',
            'as': 'todos'
        }
    }


def get_relations_for_todo() -> dict:
    """
    :return: Dictionary with ToDo relationships
    """
    return {
        'user': {
            'localField': 'user',
            'foreignField': '_id',
            'as': 'user'
        }
    }
