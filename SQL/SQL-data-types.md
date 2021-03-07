# SQL Datatypes

## Numerical datatypes
___

Name | Storage Size | Description | Range
---- | ------------ | ----------- | ----- |
**Integer** | | | |
`integer` | 4 bytes | typical choice for integer |	-2147483648 to +2147483647
`smallint` | 2 bytes | small-range integer | -32768 to +32767
`bigint` | 8 bytes | large-range integer | -9223372036854775808 to +9223372036854775807
**Floatting Point** | | | |
`real` | 4 bytes | variable-precision, inexact | 6 decimal digits precision
`double precision` | 8 bytes | variable-precision, inexact | 15 decimal digits precision
`numeric` |	variable | user-specified precision, exact | up to 131072 digits before the decimal point; up to 16383 digits after the decimal point
`decimal` |	variable | user-specified precision, exact | up to 131072 digits before the decimal point; up to 16383 digits after the decimal point
`money` | 8 bytes | currency amount | -92233720368547758.08 to +92233720368547758.07
**Serial** | | | |
`smallserial` |	2 bytes |	small autoincrementing integer | 1 to 32767
`serial` | 4 bytes | autoincrementing integer | 1 to 2147483647
`bigserial` | 8 bytes | large autoincrementing integer | 1 to 9223372036854775807

### Variable-precision and Floating Point:

The precision of a numeric is the total count of significant digits in the whole number, that is, the number of digits to both sides of the decimal point. The scale of a numeric is the count of decimal digits in the fractional part, to the right of the decimal point. So the number 23.5141 has a precision of 6 and a scale of 4. Integers can be considered to have a scale of zero.

```sql
--declare a column of type numeric
NUMERIC(precision, scale)

--23.5141 as a numeric: precision 6, scale 4
NUMERIC(6, 4)
```

Notes:

* If you require exact storage and calculations (such as for monetary amounts), use the numeric type.
* Comparing two floating-point values for equality might not always work as expected.
* In addition to ordinary numeric values, the floating-point types have several special values: `Infinity`, `-Infinity` and `NaN`

## String datatype
___
Name | Description |
---- | ----------- |
`character varying(n)`, `varchar(n)` | variable-length with limit of n positive integer |
`character(n)`, `char(n)` |	fixed-length of n positive integer, blank padded |
`text` |	variable unlimited length |


