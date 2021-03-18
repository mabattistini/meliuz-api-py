def TeamPokemonSerializer(rows, many=False):
    result = []

    def json_record(row):
        result_dict = {
            'id': row.id,
            'team': {
                'id': row.team.id,
                'name': row.team.name,
                'coach': row.team.coach,
            },
            'pokemon': {
                'id': row.pokemon.id,
                'name': row.pokemon.name,
                'height': row.pokemon.height,
                'weight': row.pokemon.weight,
                'xp': row.pokemon.xp,
                'image': row.pokemon.image,
                'types': []
            }
        }
        return result_dict

    if not many:
        result = json_record(rows)
    else:
        for row in rows:
            result.append(json_record(row))

    return result
