from database.database import supabase

def equipment_exists(id_equipment: str) -> bool:
    """
    Check whether a Equipment already exists.
    """

    response = (
        supabase
        .table("equipment")
        .select("id_equipment")
        .eq("id_equipment", id_equipment)
        .execute()
    )

    return len(response.data) > 0


def insert_equipment(
    id_equipment: str,
    name_equipment: str,
    capacity_hour: float
) -> dict:

    if equipment_exists(id_equipment):
        raise ValueError(
            f"Equipment '{id_equipment}' already exists."
        )

    response = (
        supabase
        .table("equipment")
        .insert(
            {
                "id_equipment": id_equipment,
                "name_equipment": name_equipment,
                "capacity_hour": capacity_hour
            }
        )
        .execute()
    )

    return response.data


def get_equipment(
    id_equipment: str
) -> dict | None:

    response = (
        supabase
        .table("equipment")
        .select("*")
        .eq("id_equipment", id_equipment)
        .execute()
    )

    if not response.data:
        return None

    return response.data[0]


def update_equipment(
    id_equipment: str,
    name_equipment: str,
    capacity_hour: float
) -> dict:

    response = (
        supabase
        .table("equipment")
        .update(
            {
                "name_equipment": name_equipment,
                "capacity_hour": capacity_hour
            }
        )
        .eq("id_equipment", id_equipment)
        .execute()
    )

    return response.data


def delete_equipment(
    id_equipment: str
) -> dict:

    response = (
        supabase
        .table("equipment")
        .delete()
        .eq("id_equipment", id_equipment)
        .execute()
    )

    return response.data


if __name__ == "__main__":

    try:
        result = insert_equipment(
        "CUTTER-01",
        "Main Cutter",
        500
        )
    except ValueError as e:
        print(f"Warning: {e}")