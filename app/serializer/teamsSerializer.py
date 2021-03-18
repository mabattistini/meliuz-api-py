def TeamsSerializer(rows, many=False):
    result = []

    def json_record(row):
        result_dict = {
            'id': row.id,
            'name': row.name,
            'coach': row.coach
        }
        return result_dict

    if not many:
        result = json_record(rows)
    else:
        for row in rows:
            result.append(json_record(row))

    return result
