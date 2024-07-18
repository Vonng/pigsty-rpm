# PostgreSQL Extensions for Pigsty


--------

## Common Extensions

| Extension Name                                                       |             | SPEC                                                 | Comment             |
|----------------------------------------------------------------------|-------------|------------------------------------------------------|---------------------|
| [scws](https://github.com/hightman/scws)                             | v1.2.3      | [scws.spec](SPECS/scws.spec)                         | Deps of zhparser    |
| [libduckdb](https://github.com/duckdb/duckdb)                        | v1.0.0      | [libduckdb.spec](SPECS/libduckdb.spec)               | Deps of duckdb_fdw  |
| [duckdb_fdw](https://github.com/alitrack/duckdb_fdw)                 | v1.0.0      | [pg_graphql.spec](SPECS/duckdb_fdw.spec)             |                     |
| [zhparser](https://github.com/amutu/zhparser)                        | v2.2        | [zhparser.spec](SPECS/zhparser.spec)                 |                     |
| [pg_roaringbitmap](https://github.com/ChenHuajun/pg_roaringbitmap)   | v0.5.4      | [pg_roaringbitmap.spec](SPECS/pg_roaringbitmap.spec) |                     |
| [pgjwt](https://github.com/michelp/pgjwt)                            | v0.2.0      | [pgjwt.spec](SPECS/pgjwt.spec)                       |                     |
| [vault](https://github.com/supabase/vault)                           | v0.2.9      | [vault.spec](SPECS/vault.spec)                       |                     |
| [hydra](https://github.com/hydradatabase/)                           | v1.1.2      | [hydra.spec](SPECS/hydra.spec)                       |                     |
| [age](https://github.com/apache/age)                                 | v1.5.0      | [age.spec](SPECS/age.spec)                           | 1.4 with PG15       |
| [plv8](https://github.com/plv8/plv8)                                 | v3.2.2      | [plv8.spec](SPECS/plv8)                              |                     |
| [pg_tde](https://github.com/Percona-Lab/pg_tde/tree/1.0.0-alpha)     | v1.0.0-beta | [pg_tde.spec](SPECS/pg_tde)                          |                     |
| [md5hash](https://github.com/tvondra/md5hash)                        | v1.0.1      | [md5hash.spec](SPECS/md5hash)                        |                     |


Obsolete due to included in PGDG repo:

| Extension Name                                                       |        | SPEC                                           | Comment             |
|----------------------------------------------------------------------|--------|------------------------------------------------|---------------------|
| [pg_sparse](https://github.com/paradedb/paradedb/tree/dev/pg_sparse) | v0.6.1 | [pg_sparse.spec](SPECS/pg_svector.spec)        | *Obsolete*          |
| [pg_tle](https://github.com/aws/pg_tle)                              | v1.3.4 | [pg_tle.spec](SPECS/pg_tle.spec)               |                     |
| [pg_bigm](https://github.com/pgbigm/pg_bigm)                         | v1.2   | [pg_bigm.spec](SPECS/pg_bigm.spec)             | 12 - 15             |
| [pgsql-http](https://github.com/pramsey/pgsql-http)                  | v1.6.0 | [pgsql-http.spec](SPECS/pgsql-http.spec)       |                     |
| [pgsql-gzip](https://github.com/pramsey/pgsql-gzip)                  | v1.0.0 | [pgsql-gzip.spec](SPECS/pgsql-gzip.spec)       |                     |
| [pg_net](https://github.com/supabase/pg_net)                         | v0.9.2 | [pg_net.spec](SPECS/pg_net.spec)               | no el7, el9 fix     |
| [pg_filedump](https://github.com/df7cb/pg_filedump)                  | v16.0  | [pg_filedump.spec](SPECS/pg_filedump.spec)     | el7 build with PG15 |
| [pg_dirtyread](https://github.com/df7cb/pg_dirtyread)                | v2.7   | [pg_dirtyread.spec](SPECS/pg_dirtyread)        | for el7 only        |
| [pointcloud](https://github.com/pgpointcloud/pointcloud)             | v1.2.5 | [pointcloud.spec](SPECS/pointcloud.spec)       | for el7 only        |
| [imgsmlr](https://github.com/postgrespro/imgsmlr)                    | v1.0.0 | [imgsmlr.spec](SPECS/imgsmlr.spec)             | 12 - 15             |
| [pg_similarity](https://github.com/eulerto/pg_similarity)            | v1.0.0 | [pg_similarity.spec](SPECS/pg_similarity.spec) | 12 - 15             |



**EL7 building list**

https://download.postgresql.org/pub/repos/yum/15/redhat/rhel-7.9-x86_64/

```bash
make scws scws-install
make zhparser
make pg_roaringbitmap
make pg_tle
make pgjwt
make vault
make pointcloud
make imgsmlr
make pg_similarity
make pg_bigm
make hydra
make age15
make md5hash
make pg_dirtyread
make pgsql_http
make pgsql_gzip
```

**EL8/9 building list**

https://download.postgresql.org/pub/repos/yum/16/redhat/rhel-8-x86_64
https://download.postgresql.org/pub/repos/yum/16/redhat/rhel-9-x86_64

```bash
make scws scws-install
make zhparser
make pg_roaringbitmap
make pgjwt
make vault
make imgsmlr
make pg_similarity
make hydra
make age age15
make md5hash
make pg_tde

# obsolete
# make pointcloud
# make pg_bigm
# make pg_dirtyread
# make pg_tle
```



--------

## Rust Extensions

Check [`pgrx`](pgrx.md) for RUST extensions

| Vendor        | Name                                                                       | Version | PGRX                                                                                            | License                                                                     | PG Ver         | Deps                 |
|---------------|----------------------------------------------------------------------------|---------|-------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------|----------------|----------------------|
| PostgresML    | [pgml](https://github.com/postgresml/postgresml)                           | v2.9.2  | [v0.11.3](https://github.com/postgresml/postgresml/blob/master/pgml-extension/Cargo.lock#L1785) | [MIT](https://github.com/postgresml/postgresml/blob/master/MIT-LICENSE.txt) | 16,15,14       |                      |
| ParadeDB      | [pg_search](https://github.com/paradedb/paradedb/tree/dev/pg_search)       | v0.8.4  | [v0.11.3](https://github.com/paradedb/paradedb/blob/dev/pg_search/Cargo.toml#L36)               | [AGPLv3](https://github.com/paradedb/paradedb/blob/dev/LICENSE)             | 16,15          |                      |
| ParadeDB      | [pg_lakehouse](https://github.com/paradedb/paradedb/tree/dev/pg_lakehouse) | v0.8.4  | [v0.11.3](https://github.com/paradedb/paradedb/blob/dev/pg_lakehouse/Cargo.toml#L26)            | [AGPLv3](https://github.com/paradedb/paradedb/blob/dev/LICENSE)             | 16,15          |                      |
| Supabase      | [pg_graphql](https://github.com/supabase/pg_graphql)                       | v1.5.7  | [v0.11.3](https://github.com/supabase/pg_graphql/blob/master/Cargo.toml#L17)                    | [Apache-2.0](https://github.com/supabase/pg_graphql/blob/master/LICENSE)    | 16,15          |                      |
| Supabase      | [pg_jsonschema](https://github.com/supabase/pg_jsonschema)                 | v0.3.1  | [v0.11.3](https://github.com/supabase/pg_jsonschema/blob/master/Cargo.toml#L19)                 | [Apache-2.0](https://github.com/supabase/pg_jsonschema/blob/master/LICENSE) | 16,15,14,13,12 |                      |
| Supabase      | [wrappers](https://github.com/supabase/wrappers)                           | v0.4.1  | [v0.11.3](https://github.com/supabase/wrappers/blob/main/Cargo.lock#L4254)                      | [Apache-2.0](https://github.com/supabase/wrappers/blob/main/LICENSE)        | 16,15,14       |                      |
| Tembo         | [pgmq](https://github.com/tembo-io/pgmq)                                   | v1.2.1  | v0.11.3                                                                                         | [PostgreSQL](https://github.com/tembo-io/pgmq)                              | 16,15,14,13,12 |                      |
| Tembo         | [pg_tier](https://github.com/tembo-io/pg_tier)                             | v0.0.4  | v0.11.3                                                                                         | [Apache-2.0](https://github.com/tembo-io/pg_tier/blob/main/LICENSE)         | 16             | pgmq, parquet_s3_fdw |
| Tembo         | [pg_vectorize](https://github.com/tembo-io/pg_vectorize)                   | v0.17.0 | v0.11.3                                                                                         | [PostgreSQL](https://github.com/tembo-io/pg_vectorize/blob/main/LICENSE)    | 16,15,14       | pgmq, pg_cron        |
| Tembo         | [pg_later](https://github.com/tembo-io/pg_later)                           | v0.1.1  | v0.11.3                                                                                         | [PostgreSQL](https://github.com/tembo-io/pg_later/blob/main/LICENSE)        | 16,15,14,13    | pgmq                 |
| VADOSWARE     | [pg_idkit](https://github.com/VADOSWARE/pg_idkit)                          | v0.2.3  | v0.11.3                                                                                         | [Apache-2.0](https://github.com/VADOSWARE/pg_idkit/blob/main/LICENSE)       | 16,15,14,13,12 |                      |
| pgsmcrypto    | [pgsmcrypto](https://github.com/zhuobie/pgsmcrypto)                        | v0.1.0  | v0.11.3                                                                                         | [MIT](https://github.com/zhuobie/pgsmcrypto/blob/main/LICENSE)              | 16,15,14,13,12 |                      |
| kelvich       | [pg_tiktoken](https://github.com/kelvich/pg_tiktoken)                      | v0.0.1  | [v0.10.2](https://github.com/kelvich/pg_tiktoken/blob/main/Cargo.toml)                          | [Apache-2.0](https://github.com/kelvich/pg_tiktoken/blob/main/LICENSE)      | 16,15,14,13,12 |                      |
| rustprooflabs | [pgdd](https://github.com/rustprooflabs/pgdd)                              | v0.5.2  | [v0.10.2](https://github.com/rustprooflabs/pgdd/blob/main/Cargo.toml#L25)                       | [MIT](https://github.com/zhuobie/pgsmcrypto/blob/main/LICENSE)              | 16,15,14,13,12 |                      |
| timescale     | [vectorscale](https://github.com/timescale/pgvectorscale)                  | v0.2.0  | [v0.11.4](https://github.com/timescale/pgvectorscale/blob/main/pgvectorscale/Cargo.toml#L17)    | [PostgreSQL](https://github.com/timescale/pgvectorscale/blob/main/LICENSE)  | 16,15,14,13,12 |                      |
| kaspermarstal | [plprql](https://github.com/kaspermarstal/plprql)                          | v0.1.0  | [v0.11.4](https://github.com/kaspermarstal/plprql/blob/main/Cargo.toml#L21)                     | [Apache-2.0](https://github.com/kaspermarstal/plprql/blob/main/LICENSE)     | 16,15,14,13,12 |                      |



Obsolete extension:

| Vendor        | Name                                                                       | Version | PGRX           | License                                                                     | PG Ver         | Deps                 |
|---------------|----------------------------------------------------------------------------|---------|----------------|-----------------------------------------------------------------------------|----------------|----------------------|
| ParadeDB      | [pg_analytics](https://github.com/paradedb/pg_analytics)                   | v0.6.1  | v0.12.0-alpha0 | [AGPLv3](https://github.com/paradedb/paradedb/blob/dev/LICENSE)             | 16,15          |                      |


------

## TODOLIST

- zombodb: https://github.com/zombodb/zombodb
- orioledb: https://github.com/orioledb/orioledb
- parquet_fdw: https://github.com/adjust/parquet_fdw
- hunspell https://github.com/postgrespro/hunspell_dicts


https://github.com/kouber/pg_sqlog
https://gitlab.com/pg_proctab/pg_proctab
https://github.com/dverite/postgres-shacrypt
https://github.com/postgrespro/pg_variables
https://github.com/postgrespro/aqo
https://github.com/iCyberon/pg_hashids
https://github.com/dverite/permuteseq

------

## **CHANGELIST**


pgml 2.9.2
pg_search & pg_lakehouse 0.8.4
pg_graphql 1.5.7
wrappers 0.4.1
pg_vectorize 0.17.0
pg_net 0.9.2

pgml: 2.9.1
pg_search: 0.8.1
pg_lakehouse: 0.8.1
pgmq: 1.1.1 -> 1.3.3
pg_graphql: 1.5.6

pg_tle: v1.3.4 -> v1.4.0
hydra: v1.1.1 -> v1.1.2
duckdb_fdw: v1.1.0 recompile
pgml: v2.8.1 -> v2.8.2
pg_graphql: 1.5.0 -> 1.5.2
pg_search, pg_analytics, pg_sparse: 0.5.6 -> 0.6.1



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
sudo yum groupinstall --nobest -y 'Development Tools';    # skip broken on EL8 
rpmdev-setuptree;
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
./node.yml -i files/pigsty/rpmbuild.yml

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


## Plv8

```bash
git clone git@github.com:plv8/plv8.git
cp -r ~/plv8 ~/rpmbuild/SOURCES/plv8
cd plv8; make

rpmbuild --define "pgmajorversion 16"  -ba ~/rpmbuild/SPECS/plv8.spec
rpmbuild --define "pgmajorversion 15"  -ba ~/rpmbuild/SPECS/plv8.spec
rpmbuild --define "pgmajorversion 14"  -ba ~/rpmbuild/SPECS/plv8.spec
rpmbuild --define "pgmajorversion 13"  -ba ~/rpmbuild/SPECS/plv8.spec
rpmbuild --define "pgmajorversion 12"  -ba ~/rpmbuild/SPECS/plv8.spec
```
