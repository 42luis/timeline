-- PRODUCTS
CREATE TABLE products (
    id_product VARCHAR(50) PRIMARY KEY,
    name_product VARCHAR(255) NOT NULL,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

-- EQUIPMENT
CREATE TABLE equipment (
    id_equipment VARCHAR(50) PRIMARY KEY,
    name_equipment VARCHAR(255) NOT NULL,
    capacity_hour FLOAT NOT NULL,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

-- ROUTINGS
CREATE TABLE routings (
    id_routing UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    id_product VARCHAR(50) REFERENCES products(id_product) ON DELETE CASCADE,
    id_equipment VARCHAR(50) REFERENCES equipment(id_equipment) ON DELETE CASCADE,
    cycle_time_minutes FLOAT NOT NULL,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    CONSTRAINT unique_product_equipment
    UNIQUE (id_product, id_equipment)
);