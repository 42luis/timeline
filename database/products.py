from database.database import supabase

def sku_exists(id_product: str) -> bool:
    """
    Check whether a SKU already exists.
    """

    response = (
        supabase
        .table("products")
        .select("id_product")
        .eq("id_product", id_product)
        .execute()
    )

    return len(response.data) > 0


def insert_product(
    id_product: str,
    name_product: str
) -> dict:

    if sku_exists(id_product):
        raise ValueError(
            f"SKU '{id_product}' already exists."
        )

    response = (
        supabase
        .table("products")
        .insert(
            {
                "id_product": id_product,
                "name_product": name_product
            }
        )
        .execute()
    )

    return response.data


def get_product(
    id_product: str
) -> dict | None:

    response = (
        supabase
        .table("products")
        .select("*")
        .eq("id_product", id_product)
        .execute()
    )

    if not response.data:
        return None

    return response.data[0]


def update_product(
    id_product: str,
    name_product: str
) -> dict:

    response = (
        supabase
        .table("products")
        .update(
            {
                "name_product": name_product
            }
        )
        .eq("id_product", id_product)
        .execute()
    )

    return response.data


def delete_product(
    id_product: str
) -> dict:

    response = (
        supabase
        .table("products")
        .delete()
        .eq("id_product", id_product)
        .execute()
    )

    return response.data


if __name__ == "__main__":

    result = get_product("PRD-0002")
    print(result)