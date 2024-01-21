# pg_graphql


## **Building pg_graphql**

Building `pg_graphql` 1.4.4 from source

```bash
tar -xf ~/rpmbuild/SOURCES/pg_graphql-1.4.4.tar.gz -C ~/
cd ~/pg_graphql-1.4.4
cargo pgrx install --release
```

Building 14,15,16 binaries

```bash
export PATH=/usr/pgsql-16/bin:/root/.cargo/bin:/pg/bin:/usr/share/Modules/bin:/usr/lib64/ccache:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/root/bin:/home/vagrant/.cargo/bin
cargo pgrx package # build pg 16

export PATH=/usr/pgsql-15/bin:/root/.cargo/bin:/pg/bin:/usr/share/Modules/bin:/usr/lib64/ccache:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/root/bin:/home/vagrant/.cargo/bin
cargo pgrx package # build pg 15

export PATH=/usr/pgsql-14/bin:/root/.cargo/bin:/pg/bin:/usr/share/Modules/bin:/usr/lib64/ccache:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/root/bin:/home/vagrant/.cargo/bin
cargo pgrx package # build pg 14
```




## **Packaging pg_graphql**

Copying them into `rpmbuild/SOURCES`

```bash
rm -rf ~/rpmbuild/SOURCES/pg_graphql-pg16 ~/rpmbuild/SOURCES/pg_graphql-pg15 ~/rpmbuild/SOURCES/pg_graphql-pg14; 
cp -r ~/pg_graphql-1.4.4/target/release/pg_graphql-pg16 ~/rpmbuild/SOURCES/;
cp -r ~/pg_graphql-1.4.4/target/release/pg_graphql-pg15 ~/rpmbuild/SOURCES/;
cp -r ~/pg_graphql-1.4.4/target/release/pg_graphql-pg14 ~/rpmbuild/SOURCES/;
```

Then build with `rpmbuild`

```bash
rpmbuild --without debuginfo --define "pgmajorversion 16" -ba ~/rpmbuild/SPECS/pg_graphql.spec
rpmbuild --without debuginfo --define "pgmajorversion 15" -ba ~/rpmbuild/SPECS/pg_graphql.spec
rpmbuild --without debuginfo --define "pgmajorversion 14" -ba ~/rpmbuild/SPECS/pg_graphql.spec
```