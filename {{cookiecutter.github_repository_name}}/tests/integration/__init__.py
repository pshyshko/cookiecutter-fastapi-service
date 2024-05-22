def compare_without_dynamic_fields(
    origin_object: dict, compare_object: dict, extra_dynamic_fields: list[str] = []
) -> bool:
    origin_object = origin_object.copy()
    compare_object = compare_object.copy()

    default_dynamic_fields: list[str] = ["uuid", "created_at", "updated_at", "id"]
    dynamic_fields: set[str] = set(default_dynamic_fields + extra_dynamic_fields)

    for field in dynamic_fields:
        try:
            origin_object.pop(field)
            compare_object.pop(field)
        except KeyError:
            continue

    equal_object_is: bool = origin_object == compare_object
    return equal_object_is
