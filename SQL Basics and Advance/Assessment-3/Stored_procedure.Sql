DELIMITER //

CREATE PROCEDURE GetStudentsByStatus(IN p_status BOOLEAN)
BEGIN
    SELECT *
    FROM students
    WHERE is_active = p_status;
END //

DELIMITER ;