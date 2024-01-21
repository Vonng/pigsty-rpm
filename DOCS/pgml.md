# pgml

[Latest Guide](https://postgresml.org/docs/resources/developer-docs/installation) | [Old Guide](https://postgresml.org/docs/guides/setup/v2/installation)

Install rust & dependencies

```bash
cargo install cargo-pgrx --version 0.11.2
cargo pgrx init
```

```bash
yum install -y openblas* python3.11 python3.11-devel lld
sudo alternatives --set python /usr/bin/python3.11
```


Build for PG 14 / 15 / 16

```bash
tar -xf ~/rpmbuild/SOURCES/postgresml-2.8.1.tar.gz -C ~/
cd ~/postgresml-2.8.1/pgml-extension
cd deps; rm -rf linfa;  git clone https://github.com/postgresml/linfa.git

cd ../
cargo pgrx install --release -v

export PATH=/usr/pgsql-16/bin:/root/.cargo/bin:/pg/bin:/usr/share/Modules/bin:/usr/lib64/ccache:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/root/bin:/home/vagrant/.cargo/bin
cargo pgrx package # build pg 16

export PATH=/usr/pgsql-15/bin:/root/.cargo/bin:/pg/bin:/usr/share/Modules/bin:/usr/lib64/ccache:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/root/bin:/home/vagrant/.cargo/bin
cargo pgrx package # build pg 15

export PATH=/usr/pgsql-14/bin:/root/.cargo/bin:/pg/bin:/usr/share/Modules/bin:/usr/lib64/ccache:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/root/bin:/home/vagrant/.cargo/bin
cargo pgrx package # build pg 14

```
export LDLIBS=-lstdc++fs


Copying them into `rpmbuild/SOURCES`

```bash
rm -rf ~/rpmbuild/SOURCES/pgml* 

cp -r ~/postgresml/pgml-extension/target/release/pgml-pg16 ~/rpmbuild/SOURCES/pgml_16;
cp -r ~/postgresml/pgml-extension/target/release/pgml-pg15 ~/rpmbuild/SOURCES/pgml_15;
cp -r ~/postgresml/pgml-extension/target/release/pgml-pg14 ~/rpmbuild/SOURCES/pgml_14;
```




https://postgresml.org/docs/guides/setup/v2/installation


```bash

virtualenv pgml-venv
source pgml-venv/bin/activate
pip install -r pgml-venv/requirements.txt
pip install -r pgml-venv/requirements-xformers.txt --no-dependencies

shared_preload_libraries = 'pgml,pg_stat_statements'
pgml.venv = '/absolute/path/to/your/pgml-venv'

```
update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.7 1
```



  Installing extension
     Copying control file to /usr/pgsql-15/share/extension/pgml.control
     Copying shared library to /usr/pgsql-15/lib/pgml.so
 Discovering SQL entities
  Discovered 129 SQL entities: 0 schemas (0 unique), 111 functions, 0 types, 7 enums, 1 sqls, 0 ords, 0 hashes, 10 aggregates, 0 triggers
     Writing SQL entities to /usr/pgsql-15/share/extension/pgml--2.7.8.sql
     Copying extension schema upgrade file to /usr/pgsql-15/share/extension/pgml--2.7.1--2.7.2.sql
     Copying extension schema upgrade file to /usr/pgsql-15/share/extension/pgml--2.1.1--2.1.2.sql
     Copying extension schema upgrade file to /usr/pgsql-15/share/extension/pgml--2.7.7--2.7.8.sql
     Copying extension schema upgrade file to /usr/pgsql-15/share/extension/pgml--2.5.2--2.5.3.sql
     Copying extension schema upgrade file to /usr/pgsql-15/share/extension/pgml--2.7.4--2.7.5.sql
     Copying extension schema upgrade file to /usr/pgsql-15/share/extension/pgml--2.4.5--2.4.6.sql
     Copying extension schema upgrade file to /usr/pgsql-15/share/extension/pgml--2.4.0--2.4.1.sql
     Copying extension schema upgrade file to /usr/pgsql-15/share/extension/pgml--2.3.0--2.4.0.sql
     Copying extension schema upgrade file to /usr/pgsql-15/share/extension/pgml--2.7.6--2.7.7.sql
     Copying extension schema upgrade file to /usr/pgsql-15/share/extension/pgml--2.5.0--2.5.1.sql
     Copying extension schema upgrade file to /usr/pgsql-15/share/extension/pgml--2.4.8--2.5.0.sql
     Copying extension schema upgrade file to /usr/pgsql-15/share/extension/pgml--2.4.2--2.4.3.sql
     Copying extension schema upgrade file to /usr/pgsql-15/share/extension/pgml--2.2.0--2.3.0.sql
     Copying extension schema upgrade file to /usr/pgsql-15/share/extension/pgml--2.7.3--2.7.4.sql
     Copying extension schema upgrade file to /usr/pgsql-15/share/extension/pgml--2.4.1--2.4.2.sql
     Copying extension schema upgrade file to /usr/pgsql-15/share/extension/pgml--2.4.7--2.4.8.sql
     Copying extension schema upgrade file to /usr/pgsql-15/share/extension/pgml--2.6.0--2.7.0.sql
     Copying extension schema upgrade file to /usr/pgsql-15/share/extension/pgml--2.4.4--2.4.5.sql
     Copying extension schema upgrade file to /usr/pgsql-15/share/extension/pgml--2.7.5--2.7.6.sql
     Copying extension schema upgrade file to /usr/pgsql-15/share/extension/pgml--2.7.0--2.7.1.sql
     Copying extension schema upgrade file to /usr/pgsql-15/share/extension/pgml--2.1.2--2.2.0.sql
     Copying extension schema upgrade file to /usr/pgsql-15/share/extension/pgml--2.1.0--2.1.1.sql
     Copying extension schema upgrade file to /usr/pgsql-15/share/extension/pgml--2.4.6--2.4.7.sql
     Copying extension schema upgrade file to /usr/pgsql-15/share/extension/pgml--2.0.2--2.1.0.sql
     Copying extension schema upgrade file to /usr/pgsql-15/share/extension/pgml--2.5.3--2.6.0.sql
     Copying extension schema upgrade file to /usr/pgsql-15/share/extension/pgml--2.7.2--2.7.3.sql
     Copying extension schema upgrade file to /usr/pgsql-15/share/extension/pgml--2.4.3--2.4.4.sql
     Copying extension schema upgrade file to /usr/pgsql-15/share/extension/pgml--2.5.1--2.5.2.sql

```


```
cd /tmp/postgresml/
virtualenv pgml-venv
source pgml-venv/bin/activate
cd /tmp/postgresml/pgml-extension


export PATH=/usr/pgsql-15/bin:/root/.cargo/bin:/pg/bin:/usr/share/Modules/bin:/usr/lib64/ccache:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/root/bin
cargo pgrx package # build pg 15

export PATH=/usr/pgsql-14/bin:/root/.cargo/bin:/pg/bin:/usr/share/Modules/bin:/usr/lib64/ccache:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/root/bin
cargo pgrx package # build pg 14

export PATH=/usr/pgsql-13/bin:/root/.cargo/bin:/pg/bin:/usr/share/Modules/bin:/usr/lib64/ccache:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/root/bin
cargo pgrx package # build pg 13

export PATH=/usr/pgsql-12/bin:/root/.cargo/bin:/pg/bin:/usr/share/Modules/bin:/usr/lib64/ccache:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/root/bin
cargo pgrx package # build pg 12
```





```bash
# extract from previews rpm

rm -rf /root/rpmbuild/SOURCES/pgml_15
mkdir -p /root/rpmbuild/SOURCES/pgml_15
cd /root/rpmbuild/SOURCES/pgml_15;

rpm2cpio /www/pigsty/postgresml_15-2.8.1-PIGSTY1.el8.x86_64.rpm | cpio -idmv
rpm2cpio /www/pigsty/postgresml_15-2.8.1-PIGSTY1.el9.x86_64.rpm | cpio -idmv

rpmbuild --without debuginfo --define "pgmajorversion 15" -ba /root/rpmbuild/SPECS/pgml.spec
rpmbuild --without debuginfo --define "pgmajorversion 15" -ba /root/rpmbuild/SPECS/pgml.spec

```


```bash
rpm2cpio /www/pigsty/p

```