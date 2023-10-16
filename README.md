# PostgreSQL Extensions

```bash
cd ~/rpmbuild/SEPCS

make scws
make scws-install

# simple extensions
make basic
#make zhparser pg_roaringbitmap pg_tle pgsql-http pgjwt vault hydra pg_filedump age pg_net

# rust extensions
make pg_graphql
make pgml

```



yum install pg_auth_mon_15 pg_checksums_15 pg_failover_slots_15 pg_readonly_15 postgresql-unit_15 pg_store_plans_15 pg_uuidv7_15 set_user_15



### How to Build

Download Sources

- [scws](http://www.xunsearch.com/scws/down/scws-1.2.3.tar.bz2)
- [zhparser](https://github.com/amutu/zhparser/archive/refs/tags/V2.2.tar.gz)
- [pg_embedding](https://github.com/neondatabase/pg_embedding/archive/refs/tags/0.3.6.tar.gz)
- [pg_roaringbitmap](https://github.com/ChenHuajun/pg_roaringbitmap/archive/refs/tags/v0.5.4.tar.gz)
- [apache-age](https://github.com/apache/age/releases/download/PG15%2Fv1.4.0-rc0/apache-age-1.4.0-src.tar.gz)
- [pg_tle](https://github.com/aws/pg_tle/archive/refs/tags/v1.2.0.tar.gz)
- [pgsql-http](https://github.com/pramsey/pgsql-http/archive/refs/tags/v1.6.0.tar.gz)
- [pg_net](https://github.com/supabase/pg_net/archive/refs/tags/v0.7.2.tar.gz)



```bash
yum install -y postgresql1*-server
yum install -y postgresql1*-devel
yum install -y pgdg-srpm-macros
yum install -y clang ccache perl perl-FindBin # el9 optional
dnf install perl perl-FindBin

yum install -y rpm-build rpmdevtools
yum install -y postgresql16*  # el8 el9

yum install -y flex bison krb5-devel libcurl-devel
yum install -y scws
yum install -y openssl-devel
rpmdev-setuptree;



rm -rf patroni*3.0.4*.rpm
rm -rf *docs*
```




Extra Extensions:

```bash
yum install CUnit
```
