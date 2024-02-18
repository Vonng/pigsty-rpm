# Building Rust Extensions

- PostgresML: `pgml`
- Supabase.GraphQL: `pg_graphl`
- ParadeDB.Analytics: `pg_analytics`
- ParadeDB.BM25: `pg_bm25`

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
cargo install --locked cargo-pgrx@0.11.2
HTTPS_PROXY=http://192.168.0.104:8118 cargo pgrx init 
```



----------

## Building `pg_graphql`

The latest version of `pg_graphql` is `v1.5.0`, which is compatible with `pg14`, `pg15` and `pg16`.

```bash
tar -xf ~/rpmbuild/SOURCES/pg_graphql-1.5.0.tar.gz -C ~/ ; cd ~/pg_graphql-1.5.0

export PATH=/usr/pgsql-16/bin:/root/.cargo/bin:/pg/bin:/usr/share/Modules/bin:/usr/lib64/ccache:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/root/bin:/home/vagrant/.cargo/bin;
HTTPS_PROXY=http://192.168.0.104:8118 cargo pgrx package -vvv; 
rm -rf ~/rpmbuild/SOURCES/pg_graphql_16; cp -r ~/pg_graphql-1.5.0/target/release/pg_graphql-pg16 ~/rpmbuild/SOURCES/pg_graphql_16;
rpmbuild --without debuginfo --define "pgmajorversion 16" -ba ~/rpmbuild/SPECS/pg_graphql.spec ;
 
export PATH=/usr/pgsql-15/bin:/root/.cargo/bin:/pg/bin:/usr/share/Modules/bin:/usr/lib64/ccache:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/root/bin:/home/vagrant/.cargo/bin;
HTTPS_PROXY=http://192.168.0.104:8118 cargo pgrx package -vvv;
rm -rf ~/rpmbuild/SOURCES/pg_graphql_15; cp -r ~/pg_graphql-1.5.0/target/release/pg_graphql-pg15 ~/rpmbuild/SOURCES/pg_graphql_15;
rpmbuild --without debuginfo --define "pgmajorversion 15" -ba ~/rpmbuild/SPECS/pg_graphql.spec ;

export PATH=/usr/pgsql-14/bin:/root/.cargo/bin:/pg/bin:/usr/share/Modules/bin:/usr/lib64/ccache:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/root/bin:/home/vagrant/.cargo/bin;
HTTPS_PROXY=http://192.168.0.104:8118 cargo pgrx package -vvv;
rm -rf ~/rpmbuild/SOURCES/pg_graphql_14; cp -r ~/pg_graphql-1.5.0/target/release/pg_graphql-pg14 ~/rpmbuild/SOURCES/pg_graphql_14;
rpmbuild --without debuginfo --define "pgmajorversion 14" -ba ~/rpmbuild/SPECS/pg_graphql.spec ;
```

----------------

## Building `pgml`

The latest version of `pgml` is `v2.8.1`, which is compatible with `pg14`, `pg15` and `pg16`.

```bash
sudo yum install python3.11 python3.11-devel python3-virtualenv openssl openssl-devel cmake pkg-config libomp libomp-devel openblas* llvm llvm-devel lld openblas*
sudo alternatives --set python /usr/bin/python3.11
cargo install cargo-pgrx --version 0.11.2
cargo pgrx init

git clone --recursive https://github.com/postgresml/postgresml.git
cd postgresml; git checkout v2.8.1; 
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

## Building `pg_bm25` & `pg_analytics`

The latest version of `pg_bm25` is `v0.5.6`, which is compatible with `pg16` only.

Tutorial: https://github.com/paradedb/paradedb/tree/dev/pg_analytics

```bash
git clone --recursive https://github.com/paradedb/paradedb.git
cd ~/paradedb; git checkout v0.5.6;

HTTPS_PROXY=http://192.168.0.104:8118 cargo update
```

Switch to the latest version of Rust:

```bsah
rustup update nightly
rustup override set nightly
cargo install --locked cargo-pgrx --version 0.11.2
```

Build `pg_bm25` & `pg_analytics`:

```bash
export PATH=/usr/pgsql-16/bin:/root/.cargo/bin:/pg/bin:/usr/share/Modules/bin:/usr/lib64/ccache:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/root/bin:/home/vagrant/.cargo/bin;
cd ~/paradedb/pg_bm25; HTTPS_PROXY=http://192.168.0.104:8118 cargo pgrx package  -vvv; 
cd ~/paradedb/pg_analytics; HTTPS_PROXY=http://192.168.0.104:8118 cargo pgrx package  -vvv; 

# PG15 (optional)
export PATH=/usr/pgsql-15/bin:/root/.cargo/bin:/pg/bin:/usr/share/Modules/bin:/usr/lib64/ccache:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/root/bin:/home/vagrant/.cargo/bin;
cd ~/paradedb/pg_bm25; cargo pgrx package -vvv; 
cd ~/paradedb/pg_analytics; cargo pgrx package  -vvv;
```

Packaging:

```bash
rm -rf ~/rpmbuild/SOURCES/pg_bm25_16;      cp -r ~/paradedb/target/release/pg_bm25-pg16      ~/rpmbuild/SOURCES/pg_bm25_16;
rm -rf ~/rpmbuild/SOURCES/pg_analytics_16; cp -r ~/paradedb/target/release/pg_analytics-pg16 ~/rpmbuild/SOURCES/pg_analytics_16;
rm -rf ~/rpmbuild/SOURCES/pg_bm25_15;      cp -r ~/paradedb/target/release/pg_bm25-pg15      ~/rpmbuild/SOURCES/pg_bm25_15;
rm -rf ~/rpmbuild/SOURCES/pg_analytics_15; cp -r ~/paradedb/target/release/pg_analytics-pg15 ~/rpmbuild/SOURCES/pg_analytics_15;

cd ~/rpmbuild/SPECS; make pg_bm25 pg_analytics;

rpmbuild --without debuginfo --define "pgmajorversion 16" -ba ~/rpmbuild/SPECS/pg_bm25.spec
rpmbuild --without debuginfo --define "pgmajorversion 16" -ba ~/rpmbuild/SPECS/pg_analytics.spec
rpmbuild --without debuginfo --define "pgmajorversion 15" -ba ~/rpmbuild/SPECS/pg_bm25.spec
rpmbuild --without debuginfo --define "pgmajorversion 15" -ba ~/rpmbuild/SPECS/pg_analytics.spec
```


The `pg_sparse` extension is a common C extension.

```bash
cd ~/paradedb; tar -zcf ~/rpmbuild/SOURCES/pg_sparse.tar.gz pg_sparse
```