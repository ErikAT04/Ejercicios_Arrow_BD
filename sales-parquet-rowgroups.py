import pyarrow.parquet as pq

tabla = pq.read_table('pdi_sales.parquet')
pq.write_to_dataset(tabla, root_path='sales_particionado', partition_cols=['Country'])