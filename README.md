# PostgreSQL Extensions for Pigsty

|                                                                    |        | SPEC                                                 | Comment             |
|--------------------------------------------------------------------|--------|------------------------------------------------------|---------------------|
| [scws](https://github.com/hightman/scws)                           | v1.2.3 | [scws.spec](SPECS/scws.spec)                         | Deps of zhparser    |
| [zhparser](https://github.com/amutu/zhparser)                      | v2.2   | [zhparser.spec](SPECS/zhparser.spec)                 |                     |
| [pg_roaringbitmap](https://github.com/ChenHuajun/pg_roaringbitmap) | v0.5.4 | [pg_roaringbitmap.spec](SPECS/pg_roaringbitmap.spec) |                     |
| [pg_tle](https://github.com/aws/pg_tle)                            | v1.2.0 | [pg_tle.spec](SPECS/pg_tle.spec)                     |                     |
| [pgsql-http](https://github.com/pramsey/pgsql-http)                | v1.6.0 | [pgsql-http.spec](SPECS/pgsql-http.spec)             |                     |
| [pgjwt](https://github.com/michelp/pgjwt)                          | v0.0.1 | [pgjwt.spec](SPECS/pgjwt.spec)                       |                     |
| [vault](https://github.com/supabase/vault)                         | v0.2.9 | [vault.spec](SPECS/vault.spec)                       |                     |
| [pointcloud](https://github.com/pgpointcloud/pointcloud)           | v1.2.5 | [pointcloud.spec](SPECS/pointcloud.spec)             |                     |
| [imgsmlr](https://github.com/postgrespro/imgsmlr)                  | v1.0.0 | [imgsmlr.spec](SPECS/imgsmlr.spec)                   | 12 - 15             |
| [pg_similarity](https://github.com/eulerto/pg_similarity)          | v1.0.0 | [pg_similarity.spec](SPECS/pg_similarity.spec)       | 12 - 15             |
| [pg_bigm](https://github.com/pgbigm/pg_bigm)                       | v1.2   | [pg_bigm.spec](SPECS/pg_bigm.spec)                   | 12 - 15             |
| [hydra](https://github.com/hydradatabase/)                         | v1.1.0 | [hydra.spec](SPECS/hydra.spec)                       |                     |
| [pg_net](https://github.com/supabase/pg_net)                       | v0.7.3 | [pg_net.spec](SPECS/pg_net.spec)                     | no el7              |
| https://github.com/df7cb/pg_filedump                               | v16.0  | [pg_filedump.spec](SPECS/pg_filedump.spec)           | el7 build with PG15 |
| [age](https://github.com/apache/age)                               | v1.4.0 | [age.spec](SPECS/age.spec)                           | el9 error           |
| [pg_graphql](https://github.com/supabase/pg_graphql)               | v1.4.4 | [pg_graphql.spec](SPECS/pg_graphql.spec)             | **RUST**            |
| [pgml](https://github.com/postgresml/postgresml)                   | v2.8.1 | [pgml.spec](SPECS/pgml.spec)                         | **RUST**            |



**TODOLIST**

- parquet_s3_fdw: https://github.com/pgspider/parquet_s3_fdw
- pgsql-gzip: https://github.com/pramsey/pgsql-gzip
- pg_svector: https://github.com/paradedb/paradedb/releases
- pg_bm25: https://github.com/paradedb/paradedb/releases
- zombodb: https://github.com/zombodb/zombodb
- orioledb: https://github.com/orioledb/orioledb
- duckdb_fdw: https://github.com/alitrack/duckdb_fdw



----------

## Prepare Node & Repo

Add upstream node & pgsql repo first

```bash
make build check-repo install    # setup building VMs, copy pkg.tgz and init
bin/repo-add infra node,pgsql    # add upstream repo to all 3 infra nodes
```


<details><summary>EL 8.9 Ad Hoc node Repo</summary>

EL8: `/etc/yum.repos.d/node.repo`

```ini
[baseos]
name = EL 8+ BaseOS $releasever - $basearch
baseurl = https://mirrors.aliyun.com/rockylinux/8.9/BaseOS/$basearch/os/
gpgcheck = 0
enabled = 1
module_hotfixes = 1

[appstream]
name = EL 8+ AppStream $releasever - $basearch
baseurl = https://mirrors.aliyun.com/rockylinux/8.9/AppStream/$basearch/os/
gpgcheck = 0
enabled = 1
module_hotfixes = 1

[extras]
name = EL 8+ Extras $releasever - $basearch
baseurl = https://mirrors.aliyun.com/rockylinux/8.9/extras/$basearch/os/
gpgcheck = 0
enabled = 1
module_hotfixes = 1

[PowerTools]
name = EL 8 PowerTools $releasever - $basearch
baseurl = https://mirrors.aliyun.com/rockylinux/8.9/PowerTools/$basearch/os/
gpgcheck = 0
enabled = 1
module_hotfixes = 1

[HighAvailability]
name = EL 8 PowerTools $releasever - $basearch
baseurl = https://mirrors.aliyun.com/rockylinux/8.9/HighAvailability/$basearch/os/
gpgcheck = 0
enabled = 1
module_hotfixes = 1

[NFV]
name = EL 8 NFV $releasever - $basearch
baseurl = https://mirrors.aliyun.com/rockylinux/8.9/NFV/$basearch/os/
gpgcheck = 0
enabled = 1
module_hotfixes = 1

[RT]
name = EL 8 RT $releasever - $basearch
baseurl = https://mirrors.aliyun.com/rockylinux/8.9/RT/$basearch/os/
gpgcheck = 0
enabled = 1
module_hotfixes = 1

[plus]
name = EL 8+ Extras $releasever - $basearch
baseurl = https://mirrors.aliyun.com/rockylinux/8.9/plus/$basearch/os/
gpgcheck = 0
enabled = 1
module_hotfixes = 1

[devel]
name = EL 8+ Extras $releasever - $basearch
baseurl = https://mirrors.aliyun.com/rockylinux/8.9/devel/$basearch/os/
gpgcheck = 0
enabled = 1
module_hotfixes = 1

[devel]
name = EL 8+ Extras $releasever - $basearch
baseurl = https://mirrors.aliyun.com/rockylinux/8.9/devel/$basearch/os/
gpgcheck = 0
enabled = 1
module_hotfixes = 1

[extras]
name = EL 8+ Extras $releasever - $basearch
baseurl = https://mirrors.aliyun.com/rockylinux/8.9/extras/$basearch/os/
gpgcheck = 0
enabled = 1
module_hotfixes = 1

[epel]
name = EL 8+ EPEL $releasever - $basearch
baseurl = https://mirrors.tuna.tsinghua.edu.cn/epel/8/Everything/$basearch/
gpgcheck = 0
enabled = 1
module_hotfixes = 1
```

</details>


Then add srpm repo to infra nodes

```bash
cat > /tmp/pgdg-srpm.repo <<-'EOF'
[pgdg-common-srpm]
name = PostgreSQL 15 SRPM $releasever - $basearch
baseurl=https://download.postgresql.org/pub/repos/yum/srpms/common/redhat/rhel-$releasever-x86_64/
gpgcheck = 0
enabled = 1
module_hotfixes=1
EOF
sudo mv -f /tmp/pgdg-srpm.repo /etc/yum.repos.d/pgdg-srpm.repo
sudo yum makecache
```

Finally, install compiling tools, build deps and PG major versions

```bash
sudo yum groupinstall --skip-broken -y 'Development Tools';
sudo yum install -y pgdg-srpm-macros clang ccache rpm-build rpmdevtools postgresql1*-server flex bison postgresql1*-devel readline-devel zlib-devel lz4-devel libzstd-devel openssl-devel krb5-devel libcurl-devel libxml2-devel gd-devel CUnit cmake;
sudo yum install -y python3.11 python3.11-devel python3-virtualenv openssl openssl-devel cmake pkg-config libomp libomp-devel openblas* llvm llvm-devel lld openblas* ;
sudo yum install -y createrepo_c createrepo modulemd-tools dnf-utils dnf-plugins-core yum-utils;

rpmdev-setuptree;
```

```bash
sudo alternatives --install /usr/bin/python3 python3 /usr/bin/python3.11 2
sudo alternatives --config python3
```

EL 9 Generic

```bash
# install FindBin in el9
sudo dnf install cpanminus
sudo cpanm FindBin
perl -MFindBin -e 1
```

----------

## Build PGSQL RPMs

swcs zhparser pg_roaringbitmap pg_tle pgsql-http pgjwt vault pointcloud imgsmlr pg_similarity pg_bigm hydra pg_net pg_filedump age

```bash
make push                 # push specs & sources to building machines
cd ~/rpmbuild/SPECS       # enter building context
make scws scws-install    # scws & zhparser
make el7                  # build el7 packages
make el89                 # build el8/el9 packages
make pgml                 # build pgml with RUST
make pg_graphql           # build pg_graphql with RUST

make pull                 # retrieve built packages
```


----------

## Rust Setup

Setup rust with [Tsinghua](https://mirrors.tuna.tsinghua.edu.cn/help/rustup/) [mirror](https://mirrors.tuna.tsinghua.edu.cn/help/rustup/):

```bash
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
source "$HOME/.cargo/env"
env RUSTUP_DIST_SERVER=https://mirrors.tuna.tsinghua.edu.cn/rustup rustup install stable

mkdir -vp ${CARGO_HOME:-$HOME/.cargo};
cat > ${CARGO_HOME:-$HOME/.cargo}/config << EOF
[source.crates-io]
replace-with = 'mirror'

[source.mirror]
registry = "sparse+https://mirrors.tuna.tsinghua.edu.cn/crates.io-index/"
EOF
```

Install the *latest* version of [`pgrx`](https://github.com/pgcentralfoundation/pgrx) and perform `cargo init`

```bash
cargo install --locked cargo-pgrx@0.11.2
HTTPS_PROXY=http://xxxx  cargo pgrx init 
```

----------

## Building `pg_graphql`

```bash
tar -xf ~/rpmbuild/SOURCES/pg_graphql-1.4.4.tar.gz -C ~/ ; cd ~/pg_graphql-1.4.4

export PATH=/usr/pgsql-16/bin:/root/.cargo/bin:/pg/bin:/usr/share/Modules/bin:/usr/lib64/ccache:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/root/bin:/home/vagrant/.cargo/bin;cargo pgrx package; 
rm -rf ~/rpmbuild/SOURCES/pg_graphql_16; cp -r ~/pg_graphql-1.4.4/target/release/pg_graphql-pg16 ~/rpmbuild/SOURCES/pg_graphql_16;
rpmbuild --without debuginfo --define "pgmajorversion 16" -ba ~/rpmbuild/SPECS/pg_graphql.spec ;
 
export PATH=/usr/pgsql-15/bin:/root/.cargo/bin:/pg/bin:/usr/share/Modules/bin:/usr/lib64/ccache:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/root/bin:/home/vagrant/.cargo/bin;cargo pgrx package;
rm -rf ~/rpmbuild/SOURCES/pg_graphql_15; cp -r ~/pg_graphql-1.4.4/target/release/pg_graphql-pg15 ~/rpmbuild/SOURCES/pg_graphql_15;
rpmbuild --without debuginfo --define "pgmajorversion 15" -ba ~/rpmbuild/SPECS/pg_graphql.spec ;

export PATH=/usr/pgsql-14/bin:/root/.cargo/bin:/pg/bin:/usr/share/Modules/bin:/usr/lib64/ccache:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/root/bin:/home/vagrant/.cargo/bin;cargo pgrx package;
rm -rf ~/rpmbuild/SOURCES/pg_graphql_14; cp -r ~/pg_graphql-1.4.4/target/release/pg_graphql-pg14 ~/rpmbuild/SOURCES/pg_graphql_14;
rpmbuild --without debuginfo --define "pgmajorversion 14" -ba ~/rpmbuild/SPECS/pg_graphql.spec ;
```

----------------

## Building `pgml`

Download Dependencies

```bash
sudo yum install python3.11 python3.11-devel python3-virtualenv openssl openssl-devel cmake pkg-config libomp libomp-devel openblas* llvm llvm-devel lld openblas*
sudo alternatives --set python /usr/bin/python3.11
cargo install cargo-pgrx --version 0.11.2
cargo pgrx init

git clone --recursive https://github.com/postgresml/postgresml.git
cd postgresml; git checkout v2.8.1; 
cd ~/postgresml/pgml-extension
HTTPS_PROXY=http://xxx cargo update
```

```bash
# build pg 16
export PATH=/usr/pgsql-16/bin:/root/.cargo/bin:/pg/bin:/usr/share/Modules/bin:/usr/lib64/ccache:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/root/bin:/home/vagrant/.cargo/bin;
HTTPS_PROXY=http:/xxx cargo pgrx package # build pg 16
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
+++    println!("cargo:rustc-link-lib=static=stdc++fs");
+++    println!("cargo:rustc-link-search=native=/opt/rh/gcc-toolset-13/root/usr/lib/gcc/x86_64-redhat-linux/13");
}
```

Change `Cargo.toml`

```bash
[build-dependencies]
+++ cc = "1.0"
```

</details>



----------------

## Building `duckdb_fdw`

Check duckdb release version: https://github.com/duckdb/duckdb/releases : [0.9.2](https://github.com/duckdb/duckdb/releases/tag/v0.9.2)

- [libduckdb-linux-amd64.zip](https://github.com/duckdb/duckdb/releases/download/v0.9.2/libduckdb-linux-amd64.zip)
- [libduckdb-linux-aarch64.zip](https://github.com/duckdb/duckdb/releases/download/v0.9.2/libduckdb-linux-aarch64.zip)
- [libduckdb-osx-universal.zip](https://github.com/duckdb/duckdb/releases/download/v0.9.2/libduckdb-osx-universal.zip)

```bash
git clone https://github.com/alitrack/duckdb_fdw
cd duckdb_fdw

curl -L https://github.com/duckdb/duckdb/releases/download/v0.9.2/libduckdb-linux-amd64.zip   -o libduckdb-linux-amd64.zip


curl -L https://github.com/duckdb/duckdb/releases/download/v0.9.2/libduckdb-osx-universal.zip -o libduckdb-osx-universal.zip
unzip -d . libduckdb-osx-universal.zip
cp libduckdb.dylib $(pg_config --libdir) 

make USE_PGXS=1
make install USE_PGXS=1
```