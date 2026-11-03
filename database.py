from os import getenv

from dotenv import load_dotenv
from supabase import create_client, Client


load_dotenv()


SUPABASE_URL = getenv("SUPABASE_URL")
SUPABASE_KEY = getenv("SUPABASE_KEY")

if not SUPABASE_URL or not SUPABASE_KEY:
    raise ValueError(
        "SUPABASE_URL and SUPABASE_KEY must be defined in .env"
    )


supabase: Client = create_client(
    SUPABASE_URL,
    SUPABASE_KEY
)


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
    """
    Insert a new product.
    """

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


if __name__ == "__main__":

    print(
        "Database connection configured successfully."
    )