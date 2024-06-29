# Building Rust Extensions

- PostgresML: `pgml`
- Supabase.GraphQL: `pg_graphl`
- ParadeDB.Analytics: `pg_analytics`
- ParadeDB.BM25: `pg_search`

> ParadeDB.SVector: `pg_sparse`

----------

## Rust Setup

```bash
make pgml                 # build pgml with RUST
make pg_graphql           # build pg_graphql with RUST
```

Setup rust with [Tsinghua](https://mirrors.tuna.tsinghua.edu.cn/help/rustup/) [mirror](https://mirrors.tuna.tsinghua.edu.cn/help/rustup/):

```bash
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
source "$HOME/.cargo/env"
```

Setup Mirror in Mainland China:

```bash
mkdir -vp ${CARGO_HOME:-$HOME/.cargo};
cat > ${CARGO_HOME:-$HOME/.cargo}/config << EOF
[source.crates-io]
replace-with = 'mirror'

[source.mirror]
registry = "sparse+https://mirrors.tuna.tsinghua.edu.cn/crates.io-index/"
EOF
env RUSTUP_DIST_SERVER=https://mirrors.tuna.tsinghua.edu.cn/rustup rustup install stable
```


Install the *latest* version of [`pgrx`](https://github.com/pgcentralfoundation/pgrx) and perform `cargo init`

YOU **MUST** Pass `HTTPS_PROXY` as following:

```bash
cargo install --locked cargo-pgrx@0.11.4
HTTPS_PROXY=http://192.168.0.104:8118 cargo pgrx init 
```



----------

## Building `pg_graphql`

The latest version of `pg_graphql` is `v1.5.4`, which is compatible with `pg14`, `pg15` and `pg16`.

```bash
tar -xf ~/rpmbuild/SOURCES/pg_graphql-1.5.4.tar.gz -C ~/ ; cd ~/pg_graphql-1.5.4

export PATH=/usr/pgsql-16/bin:/root/.cargo/bin:/pg/bin:/usr/share/Modules/bin:/usr/lib64/ccache:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/root/bin:/home/vagrant/.cargo/bin;
HTTPS_PROXY=http://192.168.0.104:8118 cargo pgrx package -vvv; 
rm -rf ~/rpmbuild/SOURCES/pg_graphql_16; cp -r ~/pg_graphql-1.5.3/target/release/pg_graphql-pg16 ~/rpmbuild/SOURCES/pg_graphql_16;
rpmbuild --without debuginfo --define "pgmajorversion 16" -ba ~/rpmbuild/SPECS/pg_graphql.spec ;
 
export PATH=/usr/pgsql-15/bin:/root/.cargo/bin:/pg/bin:/usr/share/Modules/bin:/usr/lib64/ccache:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/root/bin:/home/vagrant/.cargo/bin;
HTTPS_PROXY=http://192.168.0.104:8118 cargo pgrx package -vvv;
rm -rf ~/rpmbuild/SOURCES/pg_graphql_15; cp -r ~/pg_graphql-1.5.3/target/release/pg_graphql-pg15 ~/rpmbuild/SOURCES/pg_graphql_15;
rpmbuild --without debuginfo --define "pgmajorversion 15" -ba ~/rpmbuild/SPECS/pg_graphql.spec ;

export PATH=/usr/pgsql-14/bin:/root/.cargo/bin:/pg/bin:/usr/share/Modules/bin:/usr/lib64/ccache:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/root/bin:/home/vagrant/.cargo/bin;
HTTPS_PROXY=http://192.168.0.104:8118 cargo pgrx package -vvv;
rm -rf ~/rpmbuild/SOURCES/pg_graphql_14; cp -r ~/pg_graphql-1.5.3/target/release/pg_graphql-pg14 ~/rpmbuild/SOURCES/pg_graphql_14;
rpmbuild --without debuginfo --define "pgmajorversion 14" -ba ~/rpmbuild/SPECS/pg_graphql.spec ;
```

----------------

## Building `pgml`

The latest version of `pgml` is `v2.8.1`, which is compatible with `pg14`, `pg15` and `pg16`.

```bash
sudo yum install python3.11 python3.11-devel python3-virtualenv openssl openssl-devel cmake pkg-config libomp libomp-devel openblas* llvm llvm-devel lld openblas*
sudo alternatives --set python /usr/bin/python3.11

sudo alternatives --install /usr/bin/python3 python3 /usr/bin/python3.11 1
sudo alternatives --set python3 /usr/bin/python3.11

cargo install cargo-pgrx --version 0.11.3

cargo pgrx init

git clone --recursive https://github.com/postgresml/postgresml.git
cd postgresml; git checkout v2.9.1; 
cd ~/postgresml/pgml-extension
HTTPS_PROXY=http://192.168.0.104:8118 cargo update
```

```bash
# build pg 16
export PATH=/usr/pgsql-16/bin:/root/.cargo/bin:/pg/bin:/usr/share/Modules/bin:/usr/lib64/ccache:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/root/bin:/home/vagrant/.cargo/bin;
HTTPS_PROXY=http://192.168.0.104:8118 cargo pgrx package -vvv; # build pg 16
rm -rf ~/rpmbuild/SOURCES/pgml_16; cp -r ~/postgresml/pgml-extension/target/release/pgml-pg16 ~/rpmbuild/SOURCES/pgml_16;
rpmbuild --without debuginfo --define "pgmajorversion 16" -ba ~/rpmbuild/SPECS/pgml.spec

# build pg 15
export PATH=/usr/pgsql-15/bin:/root/.cargo/bin:/pg/bin:/usr/share/Modules/bin:/usr/lib64/ccache:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/root/bin:/home/vagrant/.cargo/bin;
HTTPS_PROXY=http://xxx cargo pgrx package; 
rm -rf ~/rpmbuild/SOURCES/pgml_15; cp -r ~/postgresml/pgml-extension/target/release/pgml-pg15 ~/rpmbuild/SOURCES/pgml_15;
rpmbuild --without debuginfo --define "pgmajorversion 15" -ba ~/rpmbuild/SPECS/pgml.spec

# build pg 14
export PATH=/usr/pgsql-14/bin:/root/.cargo/bin:/pg/bin:/usr/share/Modules/bin:/usr/lib64/ccache:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/root/bin:/home/vagrant/.cargo/bin;
HTTPS_PROXY=http:/xxx cargo pgrx package;
rm -rf ~/rpmbuild/SOURCES/pgml_14; cp -r ~/postgresml/pgml-extension/target/release/pgml-pg14 ~/rpmbuild/SOURCES/pgml_14;
rpmbuild --without debuginfo --define "pgmajorversion 14" -ba ~/rpmbuild/SPECS/pgml.spec
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


<details><summary>EL 8.9 Ad Hoc Building Steps</summary>

PostgresML Use C++ 17 features, you have to use GCC 10+ with static link to compile it on RockyLinux 7.x

```bash
sudo dnf install gcc-toolset-13
source /opt/rh/gcc-toolset-13/enable
export CC=/opt/rh/gcc-toolset-13/root/usr/bin/gcc
export CXX=/opt/rh/gcc-toolset-13/root/usr/bin/g++
export LD_LIBRARY_PATH=/opt/rh/gcc-toolset-13/root/usr/lib64:$LD_LIBRARY_PATH
```

Change `build.rs`:

```bash
fn main() {
    println!("cargo:rustc-link-lib=static=stdc++fs");
    println!("cargo:rustc-link-search=native=/opt/rh/gcc-toolset-13/root/usr/lib/gcc/x86_64-redhat-linux/13");
}
```

Change `Cargo.toml`

```bash
[build-dependencies]
+++ cc = "1.0"
```

</details>



----------

## Building `pg_search` & `pg_analytics`

The latest version of `pg_search` is `v0.5.6`, which is compatible with `pg16` only.

Tutorial: https://github.com/paradedb/paradedb/tree/dev/pg_analytics


```bash
# ssh -T git@github.com
Host github.com
    Hostname ssh.github.com
    Port 443
    User git
```

```bash
git clone --recursive https://github.com/paradedb/paradedb.git
cd ~/paradedb; git checkout v0.7.0;

HTTPS_PROXY=http://192.168.0.104:8118 cargo update
```

Switch to the latest version of Rust:

```bsah
rustup update nightly
rustup override set nightly
cargo install --locked cargo-pgrx --version 0.11.2
```

Build `pg_search` & `pg_analytics`:

```bash
export PATH=/usr/pgsql-16/bin:/root/.cargo/bin:/pg/bin:/usr/share/Modules/bin:/usr/lib64/ccache:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/root/bin:/home/vagrant/.cargo/bin;
cd ~/paradedb/pg_search;    HTTPS_PROXY=http://192.168.0.104:8118 cargo pgrx package  -vvv; 
cd ~/paradedb/pg_analytics; HTTPS_PROXY=http://192.168.0.104:8118 cargo pgrx package  -vvv;
cd ~/paradedb/pg_lakehouse; HTTPS_PROXY=http://192.168.0.104:8118 cargo pgrx package  -vvv; 

# PG15 (optional)
export PATH=/usr/pgsql-15/bin:/root/.cargo/bin:/pg/bin:/usr/share/Modules/bin:/usr/lib64/ccache:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/root/bin:/home/vagrant/.cargo/bin;
cd ~/paradedb/pg_search;    cargo pgrx package -vvv; 
cd ~/paradedb/pg_analytics; cargo pgrx package -vvv;
cd ~/paradedb/pg_lakehouse; cargo pgrx package -vvv;
```

Packaging:

```bash
rm -rf ~/rpmbuild/SOURCES/pg_search_16;      cp -r ~/paradedb/target/release/pg_search-pg16      ~/rpmbuild/SOURCES/pg_search_16;
rm -rf ~/rpmbuild/SOURCES/pg_analytics_16;   cp -r ~/paradedb/target/release/pg_analytics-pg16   ~/rpmbuild/SOURCES/pg_analytics_16;
rm -rf ~/rpmbuild/SOURCES/pg_search_15;      cp -r ~/paradedb/target/release/pg_search-pg15      ~/rpmbuild/SOURCES/pg_search_15;
rm -rf ~/rpmbuild/SOURCES/pg_analytics_15;   cp -r ~/paradedb/target/release/pg_analytics-pg15   ~/rpmbuild/SOURCES/pg_analytics_15;

cd ~/rpmbuild/SPECS;
make pg_search pg_analytics;

rpmbuild --without debuginfo --define "pgmajorversion 16" -ba ~/rpmbuild/SPECS/pg_search.spec
rpmbuild --without debuginfo --define "pgmajorversion 16" -ba ~/rpmbuild/SPECS/pg_analytics.spec
rpmbuild --without debuginfo --define "pgmajorversion 15" -b[pgrx_pgcentralfoundation_ce9c076b5d3e84baf3eb56475277f699228f4160.json](..%2F..%2Fpgrx_pgcentralfoundation_ce9c076b5d3e84baf3eb56475277f699228f4160.json)a ~/rpmbuild/SPECS/pg_search.spec
rpmbuild --without debuginfo --define "pgmajorversion 15" -ba ~/rpmbuild/SPECS/pg_analytics.spec
```


The `pg_sparse` extension is a common C extension.

```bash
cd ~/paradedb; tar -zcf ~/rpmbuild/SOURCES/pg_sparse.tar.gz pg_sparse
```






```bash
export PATH=/usr/pgsql-16/bin:/root/.cargo/bin:/pg/bin:/usr/share/Modules/bin:/usr/lib64/ccache:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/root/bin:/home/vagrant/.cargo/bin;

export PATH=/usr/pgsql-15/bin:/root/.cargo/bin:/pg/bin:/usr/share/Modules/bin:/usr/lib64/ccache:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/root/bin:/home/vagrant/.cargo/bin;

export PATH=/usr/pgsql-14/bin:/root/.cargo/bin:/pg/bin:/usr/share/Modules/bin:/usr/lib64/ccache:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/root/bin:/home/vagrant/.cargo/bin;

cd ~/pgmq;                     HTTPS_PROXY=http://192.168.0.104:8118 cargo pgrx package  -vv;
cd ~/pg_tier;                  HTTPS_PROXY=http://192.168.0.104:8118 cargo pgrx package  -vv;
cd ~/pg_vertorize/extension;   HTTPS_PROXY=http://192.168.0.104:8118 cargo pgrx package  -vv;
cd ~/pg_later;                 HTTPS_PROXY=http://192.168.0.104:8118 cargo pgrx package  -vv;
cd ~/plrql/plrql;              HTTPS_PROXY=http://192.168.0.104:8118 cargo pgrx package  -vv;
cd ~/pgsmcrypto;               HTTPS_PROXY=http://192.168.0.104:8118 cargo pgrx package  -vv;
cd ~/pg_idkit                  HTTPS_PROXY=http://192.168.0.104:8118 cargo pgrx package  -vv;
cd ~/pg_jsonschema;            HTTPS_PROXY=http://192.168.0.104:8118 cargo pgrx package  -vv;
cd ~/pg_graphql;               HTTPS_PROXY=http://192.168.0.104:8118 cargo pgrx package  -vv;
cd ~/wrappers/wrappers;        HTTPS_PROXY=http://192.168.0.104:8118 cargo pgrx package  -vv;

# pgrx 0.10.2
cd ~/pgdd;                     HTTPS_PROXY=http://192.168.0.104:8118 cargo pgrx package  -vvv; 
cd ~/pg_tiktoken;              HTTPS_PROXY=http://192.168.0.104:8118 cargo pgrx package  -vvv;
cd ~/prometheus_fdw;           HTTPS_PROXY=http://192.168.0.104:8118 cargo pgrx package  -vvv;
```



- [md5hash](https://github.com/tvondra/md5hash)
- [plrql](https://github.com/kaspermarstal/plprql)
- [pg_tde](https://github.com/Percona-Lab/pg_tde/tree/1.0.0-alpha)


- [pgmq](https://github.com/tembo-io/pgmq)
- [pg_tier](https://github.com/tembo-io/pg_tier)
- [pg_vertorize](https://github.com/tembo-io/pg_vectorize)
- [pg_later](https://github.com/tembo-io/pg_later)
- [prometheus_fdw](https://github.com/tembo-io/prometheus_fdw)
- [plv8](https://github.com/plv8/plv8)
