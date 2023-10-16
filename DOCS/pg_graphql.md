# pg_graphql

https://supabase.github.io/pg_graphql/installation/


**Install Rust**

Mirror: https://mirrors.tuna.tsinghua.edu.cn/help/rustup/

```bash
env RUSTUP_DIST_SERVER=https://mirrors.tuna.tsinghua.edu.cn/rustup rustup install stable # for stable

curl --proto '=https' --tlsv1.2 -sf https://sh.rustup.rs | sh
```

Add Chinese Mirror

```bash
mkdir -vp ${CARGO_HOME:-$HOME/.cargo}

cat > ${CARGO_HOME:-$HOME/.cargo}/config << EOF
[source.crates-io]
replace-with = 'mirror'

[source.mirror]
registry = "sparse+https://mirrors.tuna.tsinghua.edu.cn/crates.io-index/"
EOF
```


**Install pgrx**

```bash
cargo install --locked cargo-pgrx@0.10.2
cargo pgrx init
```


**Building PG GraphQL**

Building pg_graphql from source

```bash
tar -xf ~/rpmbuild/SOURCES/1.4.0.tar.gz -C ~/
cd ~/pg_graphql-1.4.0
cargo pgrx install --release
```

Building 14,15,16 binaries

```bash
export PATH=/usr/pgsql-16/bin:/root/.cargo/bin:/pg/bin:/usr/share/Modules/bin:/usr/lib64/ccache:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/root/bin
cargo pgrx package # build pg 16

export PATH=/usr/pgsql-15/bin:/root/.cargo/bin:/pg/bin:/usr/share/Modules/bin:/usr/lib64/ccache:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/root/bin
cargo pgrx package # build pg 15

export PATH=/usr/pgsql-14/bin:/root/.cargo/bin:/pg/bin:/usr/share/Modules/bin:/usr/lib64/ccache:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/root/bin
cargo pgrx package # build pg 14
```


Finish the build with: 

```bash

```

Copying them into `rpmbuild/SOURCES`

```bash
rm -rf /root/rpmbuild/SOURCES/pg_graphql-pg16 /root/rpmbuild/SOURCES/pg_graphql-pg15 /root/rpmbuild/SOURCES/pg_graphql-pg14; 
cp -r /root/pg_graphql-1.4.0/target/release/pg_graphql-pg16 /root/rpmbuild/SOURCES/;
cp -r /root/pg_graphql-1.4.0/target/release/pg_graphql-pg15 /root/rpmbuild/SOURCES/;
cp -r /root/pg_graphql-1.4.0/target/release/pg_graphql-pg14 /root/rpmbuild/SOURCES/;
```

Then build with `rpmbuild`

```bash
rpmbuild --without debuginfo --define "pgmajorversion 16" -ba /root/rpmbuild/SPECS/pg_graphql.spec
rpmbuild --without debuginfo --define "pgmajorversion 15" -ba /root/rpmbuild/SPECS/pg_graphql.spec
rpmbuild --without debuginfo --define "pgmajorversion 14" -ba /root/rpmbuild/SPECS/pg_graphql.spec
```