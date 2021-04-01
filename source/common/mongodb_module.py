from .relations_module import get_relation_by_model


def build_lookup_filter(references: str, model: str) -> list:
    """
    :param references: Dictionary with the names of models of the relationship
    :param model: Model name
    :return: Pipeline list
    """
    if not references:
        return []

    entities = references.split(',')
    keys_relations = get_relation_by_model(model)
    pipeline = []

    for entity in entities:
        selected = keys_relations.get(entity)
        pipeline.append(
            {
                '$lookup': {
                    'from': entity,
                    'localField': selected['localField'],
                    'foreignField': selected['foreignField'],
                    'as': selected['as']
                }
            })

    return pipeline
