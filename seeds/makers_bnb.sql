DROP TABLE IF EXISTS users;
DROP SEQUENCE IF EXISTS user_id_seq;
DROP TABLE IF EXISTS listings;
DROP SEQUENCE IF EXISTS listing_id_seq;

CREATE SEQUENCE IF NOT EXISTS user_id_seq;
CREATE TABLE IF NOT EXISTS users (id SERIAL PRIMARY KEY, email text, password text, user_name text);
CREATE SEQUENCE IF NOT EXISTS listing_id_sequence;
CREATE TABLE IF NOT EXISTS listings (id SERIAL PRIMARY KEY, name text, description text, cost int, user_id int);

INSERT INTO users (email, password, user_name) VALUES ('testemail1@example.com', 'c2852cf707649f8392a055b4598e84206f13628b6f5807b1c8a6711b2598ef42', 'Charles Boyle');
INSERT INTO users (email, password, user_name) VALUES ('testemail2@example.com', '6eee3a5257a1329afe1dceb4ce1ebe0018e63a0788313253d3ec023228521ff2', 'Amy Santiago');
INSERT INTO users (email, password, user_name) VALUES ('testemail3@example.com', '187154941ec7f71e45f09cc85f5dc956329cee757bd1f8e1b1b2f34a4d7e0600', 'Gina Linetti');

INSERT INTO listings (name, description, cost, user_id) VALUES ('Cosy Woodland Lodge', 'Embrace the quirky, cosy interiors in this romantic getaway. Open the doors to the terrace, and let the sounds of nature waft through the lodge.', 45, 1);
INSERT INTO listings (name, description, cost, user_id) VALUES ('Barn with a Vineyard View', 'Nestled in open countryside next to our vineyard on the outskirts of Bishops Stortford, an ideal base to explore East Herts & North Essex or visit London & Cambridge.', 70, 1);
INSERT INTO listings (name, description, cost, user_id) VALUES ('Luxurious treehouse', 'Clad in aromatic cedar wood, beautifully furnished - ideal  private, woodland retreat for couples. Can also comfortably sleep up to 2 children (from 5 years) on single mattresses in loft area accessed by a ladder and hatch.', 35, 2);
INSERT INTO listings (name, description, cost, user_id) VALUES ('2BD Luxury Apartment', 'Come and stay in our beautifully designed luxury apartment, right in the heart of Kidbrooke Village! Super chic and private, with incredible views of London this luxury apartment is a home from home.', 50, 3);
INSERT INTO listings (name, description, cost, user_id) VALUES ('Immaculate City Penthouse', 'A bright one bed apartment with huge 43m2 south facing terrace with stunning views of Canary Wharf. Located on Commercial Rd this 5th floor residence offers guests the perfect place to stay in East London. ', 100, 2);
INSERT INTO listings (name, description, cost, user_id) VALUES ('Snowdrop Pod Glamping', 'Snowdrop Pod is set in its own garden with stunning views overlooking the Colne Valley.  The pod offers en suite shower & toilet, kitchette with fridge and cooker and BBQ/Firepit.', 85, 1);
