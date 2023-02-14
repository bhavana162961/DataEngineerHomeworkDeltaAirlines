WITH cte AS (
    SELECT
        flightkey,
        flightnum,
        flight_dt,
        orig_arpt,
        dest_arpt,
        flightstatus,
        lastupdt
        RANK() OVER (
            PARTITION BY
                flightkey
            ORDER BY
               lastupdt  DESC
        ) AS rnk
    FROM flight leg
)
SELECT
        flightkey,
        flightnum,
        flight_dt,
        orig_arpt,
        dest_arpt,
        flightstatus,
        lastupdt
FROM cte
WHERE
    rnk = 1;
