import pyarrow.parquet as pq

# Sólo proyección: únicamente leemos dos columnas del disco
tabla = pq.read_table('pdi_sales.parquet', columns=['Country', 'Revenue'])

# Proyección + predicado: además, descartamos los row groups sin 'Germany'
tabla = pq.read_table('pdi_sales.parquet',
                      columns=['Country', 'Revenue'],
                      filters=[('Country', '=', 'Germany')])