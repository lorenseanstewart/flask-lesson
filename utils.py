

def serialize_single(row):
    dict_row = row.__dict__
    del dict_row["_sa_instance_state"]
    dict_row["created"] = str(dict_row.get("created"))
    return dict_row


def serialize_list(_list):
    return [serialize_single(row) for row in _list]
