-- Trigger to decrease quantity of item when order is put

CREATE TRIGGER item_update AFTER INSERT ON orders FOR EACH ROW UPDATE items SET quantity = quantity - NEW.number WHERE name = NEW.item_name;
