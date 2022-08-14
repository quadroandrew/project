from app.sql_scripting import sql_system

sql = sql_system

sql.delete_table(sql)

sql_insert = ['.', '.', 'The full stop symbol derives from the Greek punctuation introduced by Aristophanes of '
                        'Byzantium in the 3rd century bce. In practice, scribes mostly employed the terminal dot; the '
                        'others fell out of use and were later replaced by other symbols. From the 9th century '
                        'onwards, the full stop began appearing as a low mark (instead of a high one), and by the '
                        'time printing began in Western Europe, the lower dot was regular and then universal.']

sql.write(sql, sql_insert, True)
