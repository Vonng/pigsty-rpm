# Building Environment Setup


----------

## Prepare Node & Repo

Add upstream node & pgsql repo first

```bash
make build check-repo install    # setup building VMs, copy pkg.tgz and init
bin/repo-add infra node,pgsql    # add upstream repo to all 3 infra nodes
```

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
```

Finally, install compiling tools, build deps and PG major versions

```bash
sudo yum groupinstall --skip-broken -y 'Development Tools';
sudo yum install -y pgdg-srpm-macros clang ccache rpm-build rpmdevtools postgresql1*-server flex bison postgresql1*-devel readline-devel zlib-devel lz4-devel libzstd-devel openssl-devel krb5-devel libcurl-devel libxml2-devel gd-devel CUnit cmake;
rpmdev-setuptree;
```


----------

## Rust Setup

Setup rust with [Tsinghua](https://mirrors.tuna.tsinghua.edu.cn/help/rustup/) mirror: https://mirrors.tuna.tsinghua.edu.cn/help/rustup/

```bash
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
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
cargo pgrx init  # download postgres tarball
```

```bash
export ALL_PROXY=http://192.168.0.104:8118
HTTPS_PROXY=http://192.168.0.104:8118 cargo pgrx init 

```

----------

# Sync Building Specs

```bash
make push       # push specs & sources to building machines

cd ~/rpmbuild/SPECS

make scws
make scws-install
make zhparser

make pg_roaringbitmap
make pg_tle
make pgsql-http
make pgjwt
make vault
make pointcloud
make imgsmlr
make pg_similarity
make pg_bigm
make hydra        # el7: rpmbuild --define "pgmajorversion 15" -ba ~/rpmbuild/SPECS/pg_filedump.spec
make pg_filedump
make age
make pg_net
```

RUST extensions

```bash
make pgml
make pg_graphql
```