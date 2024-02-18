# PostgreSQL Extensions for Pigsty

|                                                                            |        | SPEC                                                 | Comment             |
|----------------------------------------------------------------------------|--------|------------------------------------------------------|---------------------|
| [scws](https://github.com/hightman/scws)                                   | v1.2.3 | [scws.spec](SPECS/scws.spec)                         | Deps of zhparser    |
| [libduckdb](https://github.com/duckdb/duckdb)                              | v0.9.2 | [libduckdb.spec](SPECS/libduckdb.spec)               | Deps of duckdb_fdw  |
| [zhparser](https://github.com/amutu/zhparser)                              | v2.2   | [zhparser.spec](SPECS/zhparser.spec)                 |                     |
| [pg_roaringbitmap](https://github.com/ChenHuajun/pg_roaringbitmap)         | v0.5.4 | [pg_roaringbitmap.spec](SPECS/pg_roaringbitmap.spec) |                     |
| [pg_tle](https://github.com/aws/pg_tle)                                    | v1.3.4 | [pg_tle.spec](SPECS/pg_tle.spec)                     |                     |
| [pgsql-http](https://github.com/pramsey/pgsql-http)                        | v1.6.0 | [pgsql-http.spec](SPECS/pgsql-http.spec)             |                     |
| [pgsql-gzip](https://github.com/pramsey/pgsql-gzip)                        | v1.0.0 | [pgsql-gzip.spec](SPECS/pgsql-gzip.spec)             |                     |
| [pgjwt](https://github.com/michelp/pgjwt)                                  | v0.0.1 | [pgjwt.spec](SPECS/pgjwt.spec)                       |                     |
| [vault](https://github.com/supabase/vault)                                 | v0.2.9 | [vault.spec](SPECS/vault.spec)                       |                     |
| [pointcloud](https://github.com/pgpointcloud/pointcloud)                   | v1.2.5 | [pointcloud.spec](SPECS/pointcloud.spec)             |                     |
| [imgsmlr](https://github.com/postgrespro/imgsmlr)                          | v1.0.0 | [imgsmlr.spec](SPECS/imgsmlr.spec)                   | 12 - 15             |
| [pg_similarity](https://github.com/eulerto/pg_similarity)                  | v1.0.0 | [pg_similarity.spec](SPECS/pg_similarity.spec)       | 12 - 15             |
| [pg_bigm](https://github.com/pgbigm/pg_bigm)                               | v1.2   | [pg_bigm.spec](SPECS/pg_bigm.spec)                   | 12 - 15             |
| [hydra](https://github.com/hydradatabase/)                                 | v1.1.1 | [hydra.spec](SPECS/hydra.spec)                       |                     |
| [pg_net](https://github.com/supabase/pg_net)                               | v0.8.0 | [pg_net.spec](SPECS/pg_net.spec)                     | no el7, el9 fix     |
| [pg_filedump](https://github.com/df7cb/pg_filedump)                        | v16.0  | [pg_filedump.spec](SPECS/pg_filedump.spec)           | el7 build with PG15 |
| [age](https://github.com/apache/age)                                       | v1.5.0 | [age.spec](SPECS/age.spec)                           | 1.4 with PG15       |
| [duckdb_fdw](https://github.com/alitrack/duckdb_fdw)                       | v1.1   | [pg_graphql.spec](SPECS/duckdb_fdw.spec)             |                     |
| [pg_sparse](https://github.com/paradedb/paradedb/tree/dev/pg_sparse)       | v0.5.6 | [pg_sparse.spec](SPECS/pg_svector.spec)              |                     |
| [pg_bm25](https://github.com/paradedb/paradedb/tree/dev/pg_bm25)           | v0.5.6 | [pg_bm25.spec](SPECS/pg_bm25.spec)                   | **RUST**, 15,16     |
| [pg_analytics](https://github.com/paradedb/paradedb/tree/dev/pg_analytics) | v0.5.6 | [pg_analytics.spec](SPECS/pg_analytics.spec)         | **RUST**, 15,16     |
| [pg_graphql](https://github.com/supabase/pg_graphql)                       | v1.5.0 | [pg_graphql.spec](SPECS/pg_graphql.spec)             | **RUST**, 12-16     |
| [pgml](https://github.com/postgresml/postgresml)                           | v2.8.1 | [pgml.spec](SPECS/pgml.spec)                         | **RUST**, 14-16     |


**TODOLIST**

- zombodb: https://github.com/zombodb/zombodb
- orioledb: https://github.com/orioledb/orioledb
- parquet_fdw: https://github.com/adjust/parquet_fdw
- parquet_s3_fdw: https://github.com/pgspider/parquet_s3_fdw


----------

## Prepare Node & Repo

Add upstream node & pgsql repo first

```bash
make build check-repo install         # setup building VMs, copy pkg.tgz and init
bin/repo-add infra node,pgsql,local   # add upstream repo to all 3 infra nodes
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
sudo yum groupinstall --skip-broken -y 'Development Tools';    # skip broken on EL8 
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
sudo cpanm FindBin; perl -MFindBin -e 1
```


----------

## Provisioning Alternative

```bash
make rpm
./node.yml -i files/pigsty/el-build.yml

sudo yum groupinstall --skip-broken -y 'Development Tools';    # skip broken on EL8
rpmdev-setuptree;

sudo alternatives --install /usr/bin/python3 python3 /usr/bin/python3.11 2
sudo alternatives --config python3
sudo cpanm FindBin; perl -MFindBin -e 1     # EL9

make pushd-sv   # on local
make push       # on sv
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
make pull                 # retrieve built packages
```
