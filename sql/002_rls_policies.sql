-- Enable RLS

ALTER TABLE products ENABLE ROW LEVEL SECURITY;
ALTER TABLE equipment ENABLE ROW LEVEL SECURITY;
ALTER TABLE routings ENABLE ROW LEVEL SECURITY;


-- PRODUCTS

CREATE POLICY products_select_anon
ON products
FOR SELECT
TO anon
USING (true);

CREATE POLICY products_insert_anon
ON products
FOR INSERT
TO anon
WITH CHECK (true);

CREATE POLICY products_update_anon
ON products
FOR UPDATE
TO anon
USING (true)
WITH CHECK (true);

CREATE POLICY products_delete_anon
ON products
FOR DELETE
TO anon
USING (true);


-- EQUIPMENT

CREATE POLICY equipment_select_anon
ON equipment
FOR SELECT
TO anon
USING (true);

CREATE POLICY equipment_insert_anon
ON equipment
FOR INSERT
TO anon
WITH CHECK (true);

CREATE POLICY equipment_update_anon
ON equipment
FOR UPDATE
TO anon
USING (true)
WITH CHECK (true);

CREATE POLICY equipment_delete_anon
ON equipment
FOR DELETE
TO anon
USING (true);


-- ROUTINGS

CREATE POLICY routings_select_anon
ON routings
FOR SELECT
TO anon
USING (true);

CREATE POLICY routings_insert_anon
ON routings
FOR INSERT
TO anon
WITH CHECK (true);

CREATE POLICY routings_update_anon
ON routings
FOR UPDATE
TO anon
USING (true)
WITH CHECK (true);

CREATE POLICY routings_delete_anon
ON routings
FOR DELETE
TO anon
USING (true);
