ALTER TABLE club
ADD CONSTRAINT chk_club_email
CHECK (
    email IS NULL
    OR email REGEXP '^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\\.[A-Za-z]{2,}$'
);