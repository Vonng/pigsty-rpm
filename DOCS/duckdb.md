# duckdb & libduckdb & duckdb_fdw

----------------

## Building `duckdb_fdw`

Check duckdb release version: https://github.com/duckdb/duckdb/releases : [0.9.2](https://github.com/duckdb/duckdb/releases/tag/v0.9.2)

- [libduckdb-linux-amd64.zip](https://github.com/duckdb/duckdb/releases/download/v0.9.2/libduckdb-linux-amd64.zip)
- [libduckdb-linux-aarch64.zip](https://github.com/duckdb/duckdb/releases/download/v0.9.2/libduckdb-linux-aarch64.zip)
- [libduckdb-osx-universal.zip](https://github.com/duckdb/duckdb/releases/download/v0.9.2/libduckdb-osx-universal.zip)

```bash
git clone https://github.com/alitrack/duckdb_fdw
cd duckdb_fdw

# linux libduckdb
curl -L https://github.com/duckdb/duckdb/releases/download/v0.9.2/libduckdb-linux-amd64.zip   -o libduckdb-linux-amd64.zip
unzip -d . libduckdb-linux-amd64.zip
cp libduckdb.so $(pg_config --libdir)

# build extension
make USE_PGXS=1
make install USE_PGXS=1
```


```bash
make 
```




```bash
libduckdb:
	rm -rf ~/rpmbuild/RPMS/x86_64/libduckdb*.rpm;
	rpmbuild -ba ~/rpmbuild/SPECS/libduckdb.spec

duckdb_fdw:
	rpmbuild --define "pgmajorversion 12" -ba ~/rpmbuild/SPECS/duckdb_fdw.spec
	rpmbuild --define "pgmajorversion 13" -ba ~/rpmbuild/SPECS/duckdb_fdw.spec
	rpmbuild --define "pgmajorversion 14" -ba ~/rpmbuild/SPECS/duckdb_fdw.spec
	rpmbuild --define "pgmajorversion 15" -ba ~/rpmbuild/SPECS/duckdb_fdw.spec
	rpmbuild --define "pgmajorversion 16" -ba ~/rpmbuild/SPECS/duckdb_fdw.spec
```



```bash
# darwin libduckdb
curl -L https://github.com/duckdb/duckdb/releases/download/v0.9.2/libduckdb-osx-universal.zip -o libduckdb-osx-universal.zip
unzip -d . libduckdb-osx-universal.zip
cp libduckdb.dylib $(pg_config --libdir)
```



## How to use duckdb fdw ?

https://github.com/alitrack/duckdb_fdw

```bash
duckdb /tmp/duck.db

CREATE TABLE t1 (
  a integer,
  b text
);
  
INSERT INTO t1 VALUES (1, 'a'), (2 , 'b'), (3, 'c');
SELECT * FROM t1;
```


```sql
IMPORT FOREIGN SCHEMA public FROM SERVER duckdb_server INTO public;
```


```sql
CREATE EXTENSION duckdb_fdw;
CREATE SERVER duckdb_server FOREIGN DATA WRAPPER duckdb_fdw OPTIONS (database '/tmp/duck.db');
GRANT USAGE ON FOREIGN SERVER duckdb_server TO PUBLIC;
 
CREATE FOREIGN TABLE t1 (
  a integer,
  b text
)
SERVER duckdb_server
OPTIONS (table 't1');

INSERT INTO t1 VALUES (1, 'a'), (2 , 'b'), (3, 'c');
SELECT * FROM t1;
```



