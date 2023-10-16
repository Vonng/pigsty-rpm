# pgPointCloud


https://pgpointcloud.github.io/pointcloud/development.html#build-install

```bash
yum install -y libxml2-devel CUnit cmake
```



```bash
tar -xf  /root/rpmbuild/SOURCES/laz-perf-3.4.0.tar.gz -C ~/ ; cd ~/laz-perf-3.4.0/
mkdir -p build; cd build
cmake ..
make
sudo make install
```

```bash
Install the project...
-- Install configuration: "Release"
-- Installing: /usr/local/lib/cmake/LAZPERF/lazperf-targets.cmake
-- Installing: /usr/local/lib/cmake/LAZPERF/lazperf-targets-release.cmake
-- Installing: /usr/local/lib/cmake/LAZPERF/lazperf-config.cmake
-- Installing: /usr/local/lib/cmake/LAZPERF/lazperf-config-version.cmake
-- Installing: /usr/local/lib/liblazperf.so
-- Installing: /usr/local/include/lazperf/lazperf.hpp
-- Installing: /usr/local/include/lazperf/filestream.hpp
-- Installing: /usr/local/include/lazperf/header.hpp
-- Installing: /usr/local/include/lazperf/readers.hpp
-- Installing: /usr/local/include/lazperf/vlr.hpp
-- Installing: /usr/local/include/lazperf/writers.hpp
-- Installing: /usr/local/include/lazperf/lazperf_base.hpp
[root@el8 build]# cd ~/pointcloud-1.2.5/
[root@el8 pointcloud-1.2.5]# ./autogen.sh
* Running /usr/bin/aclocal (1.16.1)
* Running /usr/bin/autoconf (2.69)
======================================
```

```bash
tar -xf  /root/rpmbuild/SOURCES/pointcloud-1.2.5.tar.gz -C ~/
cd ~/pointcloud-1.2.5/
./autogen.sh
./configure --with-pgconfig=/usr/pgsql-15/bin/pg_config --with-xml2config=/usr/bin/xml2-config --with-lazperf=/usr/local/lib/liblaszip.so
PATH=/usr/pgsql-15/bin:/usr/bin/:$PATH make


```



```bash
make[1]: Entering directory '/root/pointcloud-1.2.5/pgsql'
/usr/bin/mkdir -p '/usr/pgsql-15/lib'
/usr/bin/mkdir -p '/usr/pgsql-15/share/extension'
/usr/bin/mkdir -p '/usr/pgsql-15/share/extension'
/usr/bin/install -c -m 755  pointcloud-1.2.so '/usr/pgsql-15/lib/pointcloud-1.2.so'
/usr/bin/install -c -m 644 .//pointcloud.control '/usr/pgsql-15/share/extension/'
/usr/bin/install -c -m 644  pointcloud.control pointcloud--1.2.5.sql pointcloud--1.1.0--1.2.5.sql pointcloud--1.1.1--1.2.5.sql pointcloud--1.2.0--1.2.5.sql pointcloud--1.2.1--1.2.5.sql pointcloud--1.2.2--1.2.5.sql pointcloud--1.2.3--1.2.5.sql pointcloud--1.2.4--1.2.5.sql pointcloud--1.2.5--1.2.5next.sql pointcloud--1.2.5next--1.2.5.sql '/usr/pgsql-15/share/extension/'
/usr/bin/mkdir -p '/usr/pgsql-15/lib/bitcode/pointcloud-1.2'
/usr/bin/mkdir -p '/usr/pgsql-15/lib/bitcode'/pointcloud-1.2/
/usr/bin/install -c -m 644 pc_inout.bc '/usr/pgsql-15/lib/bitcode'/pointcloud-1.2/./
/usr/bin/install -c -m 644 pc_access.bc '/usr/pgsql-15/lib/bitcode'/pointcloud-1.2/./
/usr/bin/install -c -m 644 pc_editor.bc '/usr/pgsql-15/lib/bitcode'/pointcloud-1.2/./
/usr/bin/install -c -m 644 pc_pgsql.bc '/usr/pgsql-15/lib/bitcode'/pointcloud-1.2/./
cd '/usr/pgsql-15/lib/bitcode' && /usr/bin/llvm-lto -thinlto -thinlto-action=thinlink -o pointcloud-1.2.index.bc pointcloud-1.2/pc_inout.bc pointcloud-1.2/pc_access.bc pointcloud-1.2/pc_editor.bc pointcloud-1.2/pc_pgsql.bc
make[1]: Leaving directory '/root/pointcloud-1.2.5/pgsql'
make -C pgsql_postgis install
make[1]: Entering directory '/root/pointcloud-1.2.5/pgsql_postgis'
/usr/bin/mkdir -p '/usr/pgsql-15/share/extension'
/usr/bin/mkdir -p '/usr/pgsql-15/share/extension'
/usr/bin/install -c -m 644 .//pointcloud_postgis.control '/usr/pgsql-15/share/extension/'
/usr/bin/install -c -m 644  pointcloud_postgis.control pointcloud_postgis--1.2.5.sql pointcloud_postgis--1.1.0--1.2.5.sql pointcloud_postgis--1.1.1--1.2.5.sql pointcloud_postgis--1.2.0--1.2.5.sql pointcloud_postgis--1.2.1--1.2.5.sql pointcloud_postgis--1.2.2--1.2.5.sql pointcloud_postgis--1.2.3--1.2.5.sql pointcloud_postgis--1.2.4--1.2.5.sql pointcloud_postgis--1.2.5--1.2.5next.sql pointcloud_postgis--1.2.5next--1.2.5.sql '/usr/pgsql-15/share/extension/'
make[1]: Leaving directory '/root/pointcloud-1.2.5/pgsql_postgis'
[root@el8 pointcloud-1.2.5]# pp
```




### Parquet S3 FDW

https://github.com/pgspider/parquet_s3_fdw

```bash
tar -xf  /root/rpmbuild/SOURCES/parquet_s3_fdw-1.0.0.tar.gz -C ~/


PATH=/usr/pgsql-15/bin:/root/.cargo/bin:/pg/bin:/usr/share/Modules/bin:/usr/lib64/ccache:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/root/bin make 

```
