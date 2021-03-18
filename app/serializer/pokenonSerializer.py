from app.models.pokemon import TypesModel


def pokemon_serializer(rows, many=False):
    result = []

    def json_record(row):
        result_dict = {
            'id': row.id,
            'name': row.name,
            'height': row.height,
            'weight': row.weight,
            'xp': row.xp,
            'image': row.image,
            'types': []
        }

        for row_type in row.types:
            result_dict['types'].append(row_type.name)

        return result_dict

    if not many:
        result = json_record(rows)
    else:
        for row in rows:
            if isinstance(row, TypesModel):
                result.append(json_record(row.pokemon))
            else:
                result.append(json_record(row))

    return result
