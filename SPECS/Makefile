#---------------------------------------------#
# EL
#---------------------------------------------#
default:
	echo "make make basic"

#---------------------------------------------#
# scws
#---------------------------------------------#
scws:
	rm -rf ~/rpmbuild/RPMS/x86_64/scws*.rpm /tmp/pigsty-rpm/RPMS/scws*.rpm
	QA_RPATHS=2 rpmbuild -ba ~/rpmbuild/SPECS/scws.spec

# scws is required when building zhparser
scws-install:
	sudo yum remove -y scws || /bin/true
	sudo rpm -ivh ~/rpmbuild/RPMS/x86_64/scws-1.2.3-1PIGSTY.el*.x86_64.rpm

# pure-C or pure-SQL extensions
basic:
	make zhparser pg_roaringbitmap pg_tle pgsql_http pgjwt vault hydra pg_filedump pg_net pointcloud # age

#---------------------------------------------#
# zhparser
#---------------------------------------------#
zhparser:
	rm -rf ~/rpmbuild/RPMS/x86_64/zhparser*.rpm;
	QA_RPATHS=2 rpmbuild --define "pgmajorversion 12" -ba ~/rpmbuild/SPECS/zhparser.spec
	QA_RPATHS=2 rpmbuild --define "pgmajorversion 13" -ba ~/rpmbuild/SPECS/zhparser.spec
	QA_RPATHS=2 rpmbuild --define "pgmajorversion 14" -ba ~/rpmbuild/SPECS/zhparser.spec
	QA_RPATHS=2 rpmbuild --define "pgmajorversion 15" -ba ~/rpmbuild/SPECS/zhparser.spec
	QA_RPATHS=2 rpmbuild --define "pgmajorversion 16" -ba ~/rpmbuild/SPECS/zhparser.spec   # not available on el7


#---------------------------------------------#
# hunspell
#---------------------------------------------#
hunspell: hunspell_cs_cz hunspell_de_de hunspell_en_us hunspell_fr hunspell_ne_np hunspell_nl_nl hunspell_nn_no hunspell_pt_pt hunspell_ru_ru hunspell_ru_ru_aot

hunspell_cs_cz:
	rm -rf ~/rpmbuild/RPMS/x86_64/hunspell_cs_cz*.rpm;
	rpmbuild --without debuginfo --define "pgmajorversion 12" -ba ~/rpmbuild/SPECS/hunspell_cs_cz.spec
	rpmbuild --without debuginfo --define "pgmajorversion 13" -ba ~/rpmbuild/SPECS/hunspell_cs_cz.spec
	rpmbuild --without debuginfo --define "pgmajorversion 14" -ba ~/rpmbuild/SPECS/hunspell_cs_cz.spec
	rpmbuild --without debuginfo --define "pgmajorversion 15" -ba ~/rpmbuild/SPECS/hunspell_cs_cz.spec
	rpmbuild --without debuginfo --define "pgmajorversion 16" -ba ~/rpmbuild/SPECS/hunspell_cs_cz.spec
hunspell_de_de:
	rm -rf ~/rpmbuild/RPMS/x86_64/hunspell_de_de*.rpm;
	rpmbuild --without debuginfo --define "pgmajorversion 12" -ba ~/rpmbuild/SPECS/hunspell_de_de.spec
	rpmbuild --without debuginfo --define "pgmajorversion 13" -ba ~/rpmbuild/SPECS/hunspell_de_de.spec
	rpmbuild --without debuginfo --define "pgmajorversion 14" -ba ~/rpmbuild/SPECS/hunspell_de_de.spec
	rpmbuild --without debuginfo --define "pgmajorversion 15" -ba ~/rpmbuild/SPECS/hunspell_de_de.spec
	rpmbuild --without debuginfo --define "pgmajorversion 16" -ba ~/rpmbuild/SPECS/hunspell_de_de.spec
hunspell_en_us:
	rm -rf ~/rpmbuild/RPMS/x86_64/hunspell_en_us*.rpm;
	rpmbuild --without debuginfo --define "pgmajorversion 12" -ba ~/rpmbuild/SPECS/hunspell_en_us.spec
	rpmbuild --without debuginfo --define "pgmajorversion 13" -ba ~/rpmbuild/SPECS/hunspell_en_us.spec
	rpmbuild --without debuginfo --define "pgmajorversion 14" -ba ~/rpmbuild/SPECS/hunspell_en_us.spec
	rpmbuild --without debuginfo --define "pgmajorversion 15" -ba ~/rpmbuild/SPECS/hunspell_en_us.spec
	rpmbuild --without debuginfo --define "pgmajorversion 16" -ba ~/rpmbuild/SPECS/hunspell_en_us.spec
hunspell_fr:
	rm -rf ~/rpmbuild/RPMS/x86_64/hunspell_fr*.rpm;
	rpmbuild --without debuginfo --define "pgmajorversion 12" -ba ~/rpmbuild/SPECS/hunspell_fr.spec
	rpmbuild --without debuginfo --define "pgmajorversion 13" -ba ~/rpmbuild/SPECS/hunspell_fr.spec
	rpmbuild --without debuginfo --define "pgmajorversion 14" -ba ~/rpmbuild/SPECS/hunspell_fr.spec
	rpmbuild --without debuginfo --define "pgmajorversion 15" -ba ~/rpmbuild/SPECS/hunspell_fr.spec
	rpmbuild --without debuginfo --define "pgmajorversion 16" -ba ~/rpmbuild/SPECS/hunspell_fr.spec
hunspell_ne_np:
	rm -rf ~/rpmbuild/RPMS/x86_64/hunspell_ne_np*.rpm;
	rpmbuild --without debuginfo --define "pgmajorversion 12" -ba ~/rpmbuild/SPECS/hunspell_ne_np.spec
	rpmbuild --without debuginfo --define "pgmajorversion 13" -ba ~/rpmbuild/SPECS/hunspell_ne_np.spec
	rpmbuild --without debuginfo --define "pgmajorversion 14" -ba ~/rpmbuild/SPECS/hunspell_ne_np.spec
	rpmbuild --without debuginfo --define "pgmajorversion 15" -ba ~/rpmbuild/SPECS/hunspell_ne_np.spec
	rpmbuild --without debuginfo --define "pgmajorversion 16" -ba ~/rpmbuild/SPECS/hunspell_ne_np.spec
hunspell_nl_nl:
	rm -rf ~/rpmbuild/RPMS/x86_64/hunspell_nl_nl*.rpm;
	rpmbuild --without debuginfo --define "pgmajorversion 12" -ba ~/rpmbuild/SPECS/hunspell_nl_nl.spec
	rpmbuild --without debuginfo --define "pgmajorversion 13" -ba ~/rpmbuild/SPECS/hunspell_nl_nl.spec
	rpmbuild --without debuginfo --define "pgmajorversion 14" -ba ~/rpmbuild/SPECS/hunspell_nl_nl.spec
	rpmbuild --without debuginfo --define "pgmajorversion 15" -ba ~/rpmbuild/SPECS/hunspell_nl_nl.spec
	rpmbuild --without debuginfo --define "pgmajorversion 16" -ba ~/rpmbuild/SPECS/hunspell_nl_nl.spec
hunspell_nn_no:
	rm -rf ~/rpmbuild/RPMS/x86_64/hunspell_nn_no*.rpm;
	rpmbuild --without debuginfo --define "pgmajorversion 12" -ba ~/rpmbuild/SPECS/hunspell_nn_no.spec
	rpmbuild --without debuginfo --define "pgmajorversion 13" -ba ~/rpmbuild/SPECS/hunspell_nn_no.spec
	rpmbuild --without debuginfo --define "pgmajorversion 14" -ba ~/rpmbuild/SPECS/hunspell_nn_no.spec
	rpmbuild --without debuginfo --define "pgmajorversion 15" -ba ~/rpmbuild/SPECS/hunspell_nn_no.spec
	rpmbuild --without debuginfo --define "pgmajorversion 16" -ba ~/rpmbuild/SPECS/hunspell_nn_no.spec
hunspell_pt_pt:
	rm -rf ~/rpmbuild/RPMS/x86_64/hunspell_pt_pt*.rpm;
	rpmbuild --without debuginfo --define "pgmajorversion 12" -ba ~/rpmbuild/SPECS/hunspell_pt_pt.spec
	rpmbuild --without debuginfo --define "pgmajorversion 13" -ba ~/rpmbuild/SPECS/hunspell_pt_pt.spec
	rpmbuild --without debuginfo --define "pgmajorversion 14" -ba ~/rpmbuild/SPECS/hunspell_pt_pt.spec
	rpmbuild --without debuginfo --define "pgmajorversion 15" -ba ~/rpmbuild/SPECS/hunspell_pt_pt.spec
	rpmbuild --without debuginfo --define "pgmajorversion 16" -ba ~/rpmbuild/SPECS/hunspell_pt_pt.spec
hunspell_ru_ru:
	rm -rf ~/rpmbuild/RPMS/x86_64/hunspell_ru_ru*.rpm;
	rpmbuild --without debuginfo --define "pgmajorversion 12" -ba ~/rpmbuild/SPECS/hunspell_ru_ru.spec
	rpmbuild --without debuginfo --define "pgmajorversion 13" -ba ~/rpmbuild/SPECS/hunspell_ru_ru.spec
	rpmbuild --without debuginfo --define "pgmajorversion 14" -ba ~/rpmbuild/SPECS/hunspell_ru_ru.spec
	rpmbuild --without debuginfo --define "pgmajorversion 15" -ba ~/rpmbuild/SPECS/hunspell_ru_ru.spec
	rpmbuild --without debuginfo --define "pgmajorversion 16" -ba ~/rpmbuild/SPECS/hunspell_ru_ru.spec
hunspell_ru_ru_aot:
	rm -rf ~/rpmbuild/RPMS/x86_64/hunspell_ru_ru_aot*.rpm;
	rpmbuild --without debuginfo --define "pgmajorversion 12" -ba ~/rpmbuild/SPECS/hunspell_ru_ru_aot.spec
	rpmbuild --without debuginfo --define "pgmajorversion 13" -ba ~/rpmbuild/SPECS/hunspell_ru_ru_aot.spec
	rpmbuild --without debuginfo --define "pgmajorversion 14" -ba ~/rpmbuild/SPECS/hunspell_ru_ru_aot.spec
	rpmbuild --without debuginfo --define "pgmajorversion 15" -ba ~/rpmbuild/SPECS/hunspell_ru_ru_aot.spec
	rpmbuild --without debuginfo --define "pgmajorversion 16" -ba ~/rpmbuild/SPECS/hunspell_ru_ru_aot.spec

#---------------------------------------------#
# pg_roaringbitmap
#---------------------------------------------#
pg_roaringbitmap:
	rm -rf ~/rpmbuild/RPMS/x86_64/pg_roaringbitmap*.rpm;
	rpmbuild --define "pgmajorversion 12" -ba ~/rpmbuild/SPECS/pg_roaringbitmap.spec
	rpmbuild --define "pgmajorversion 13" -ba ~/rpmbuild/SPECS/pg_roaringbitmap.spec
	rpmbuild --define "pgmajorversion 14" -ba ~/rpmbuild/SPECS/pg_roaringbitmap.spec
	rpmbuild --define "pgmajorversion 15" -ba ~/rpmbuild/SPECS/pg_roaringbitmap.spec
	rpmbuild --define "pgmajorversion 16" -ba ~/rpmbuild/SPECS/pg_roaringbitmap.spec   # not available on el7

#---------------------------------------------#
# pg_tle (deps: krb5-devel) rename to v1.4.0
#---------------------------------------------#
pg_tle:
	rm -rf ~/rpmbuild/RPMS/x86_64/pg_tle*.rpm;
	rpmbuild --define "pgmajorversion 12" -ba ~/rpmbuild/SPECS/pg_tle.spec
	rpmbuild --define "pgmajorversion 13" -ba ~/rpmbuild/SPECS/pg_tle.spec
	rpmbuild --define "pgmajorversion 14" -ba ~/rpmbuild/SPECS/pg_tle.spec
	rpmbuild --define "pgmajorversion 15" -ba ~/rpmbuild/SPECS/pg_tle.spec
	rpmbuild --define "pgmajorversion 16" -ba ~/rpmbuild/SPECS/pg_tle.spec   # not available on el7


#---------------------------------------------#
# pgjwt
#---------------------------------------------#
pgjwt:
	rm -rf ~/rpmbuild/RPMS/x86_64/pgjwt*.rpm;
	rpmbuild --without debuginfo --define "pgmajorversion 12" -ba ~/rpmbuild/SPECS/pgjwt.spec
	rpmbuild --without debuginfo --define "pgmajorversion 13" -ba ~/rpmbuild/SPECS/pgjwt.spec
	rpmbuild --without debuginfo --define "pgmajorversion 14" -ba ~/rpmbuild/SPECS/pgjwt.spec
	rpmbuild --without debuginfo --define "pgmajorversion 15" -ba ~/rpmbuild/SPECS/pgjwt.spec
	rpmbuild --without debuginfo --define "pgmajorversion 16" -ba ~/rpmbuild/SPECS/pgjwt.spec

#---------------------------------------------#
# pg_sqlog
#---------------------------------------------#
pg_sqlog:
	rm -rf ~/rpmbuild/RPMS/x86_64/pg_sqlog*.rpm;
	rpmbuild --without debuginfo --define "pgmajorversion 16" -ba ~/rpmbuild/SPECS/pg_sqlog.spec
	rpmbuild --without debuginfo --define "pgmajorversion 15" -ba ~/rpmbuild/SPECS/pg_sqlog.spec
	rpmbuild --without debuginfo --define "pgmajorversion 14" -ba ~/rpmbuild/SPECS/pg_sqlog.spec
	rpmbuild --without debuginfo --define "pgmajorversion 13" -ba ~/rpmbuild/SPECS/pg_sqlog.spec
	rpmbuild --without debuginfo --define "pgmajorversion 12" -ba ~/rpmbuild/SPECS/pg_sqlog.spec

#---------------------------------------------#
# pg_proctab
#---------------------------------------------#
pg_proctab:
	rm -rf ~/rpmbuild/RPMS/x86_64/pg_proctab*.rpm;
	rpmbuild --without debuginfo --define "pgmajorversion 16" -ba ~/rpmbuild/SPECS/pg_proctab.spec
	rpmbuild --without debuginfo --define "pgmajorversion 15" -ba ~/rpmbuild/SPECS/pg_proctab.spec
	rpmbuild --without debuginfo --define "pgmajorversion 14" -ba ~/rpmbuild/SPECS/pg_proctab.spec
	rpmbuild --without debuginfo --define "pgmajorversion 13" -ba ~/rpmbuild/SPECS/pg_proctab.spec
	rpmbuild --without debuginfo --define "pgmajorversion 12" -ba ~/rpmbuild/SPECS/pg_proctab.spec

#---------------------------------------------#
# pg_hashids
#---------------------------------------------#
pg_hashids:
	rm -rf ~/rpmbuild/RPMS/x86_64/pg_hashids*.rpm;
	rpmbuild --without debuginfo --define "pgmajorversion 16" -ba ~/rpmbuild/SPECS/pg_hashids.spec
	rpmbuild --without debuginfo --define "pgmajorversion 15" -ba ~/rpmbuild/SPECS/pg_hashids.spec
	rpmbuild --without debuginfo --define "pgmajorversion 14" -ba ~/rpmbuild/SPECS/pg_hashids.spec
	rpmbuild --without debuginfo --define "pgmajorversion 13" -ba ~/rpmbuild/SPECS/pg_hashids.spec
	rpmbuild --without debuginfo --define "pgmajorversion 12" -ba ~/rpmbuild/SPECS/pg_hashids.spec

#---------------------------------------------#
# postgres_shacrypt
#---------------------------------------------#
postgres_shacrypt:
	rm -rf ~/rpmbuild/RPMS/x86_64/postgres_shacrypt*.rpm;
	rpmbuild --without debuginfo --define "pgmajorversion 16" -ba ~/rpmbuild/SPECS/postgres_shacrypt.spec
	rpmbuild --without debuginfo --define "pgmajorversion 15" -ba ~/rpmbuild/SPECS/postgres_shacrypt.spec
	rpmbuild --without debuginfo --define "pgmajorversion 14" -ba ~/rpmbuild/SPECS/postgres_shacrypt.spec
	rpmbuild --without debuginfo --define "pgmajorversion 13" -ba ~/rpmbuild/SPECS/postgres_shacrypt.spec
	rpmbuild --without debuginfo --define "pgmajorversion 12" -ba ~/rpmbuild/SPECS/postgres_shacrypt.spec

#---------------------------------------------#
# permuteseq
#---------------------------------------------#
permuteseq:
	rm -rf ~/rpmbuild/RPMS/x86_64/permuteseq*.rpm;
	rpmbuild --without debuginfo --define "pgmajorversion 16" -ba ~/rpmbuild/SPECS/permuteseq.spec
	rpmbuild --without debuginfo --define "pgmajorversion 15" -ba ~/rpmbuild/SPECS/permuteseq.spec
	rpmbuild --without debuginfo --define "pgmajorversion 14" -ba ~/rpmbuild/SPECS/permuteseq.spec
	rpmbuild --without debuginfo --define "pgmajorversion 13" -ba ~/rpmbuild/SPECS/permuteseq.spec
	rpmbuild --without debuginfo --define "pgmajorversion 12" -ba ~/rpmbuild/SPECS/permuteseq.spec

#---------------------------------------------#
# vault
#---------------------------------------------#
vault:
	rm -rf ~/rpmbuild/RPMS/x86_64/vault*.rpm;
	rpmbuild --without debuginfo --define "pgmajorversion 12" -ba ~/rpmbuild/SPECS/vault.spec
	rpmbuild --without debuginfo --define "pgmajorversion 13" -ba ~/rpmbuild/SPECS/vault.spec
	rpmbuild --without debuginfo --define "pgmajorversion 14" -ba ~/rpmbuild/SPECS/vault.spec
	rpmbuild --without debuginfo --define "pgmajorversion 15" -ba ~/rpmbuild/SPECS/vault.spec
	rpmbuild --without debuginfo --define "pgmajorversion 16" -ba ~/rpmbuild/SPECS/vault.spec

#---------------------------------------------#
# supautils
#---------------------------------------------#
supautils:
	rm -rf ~/rpmbuild/RPMS/x86_64/supautils*.rpm;
	rpmbuild --without debuginfo --define "pgmajorversion 13" -ba ~/rpmbuild/SPECS/supautils.spec
	rpmbuild --without debuginfo --define "pgmajorversion 14" -ba ~/rpmbuild/SPECS/supautils.spec
	rpmbuild --without debuginfo --define "pgmajorversion 15" -ba ~/rpmbuild/SPECS/supautils.spec
	rpmbuild --without debuginfo --define "pgmajorversion 16" -ba ~/rpmbuild/SPECS/supautils.spec

#---------------------------------------------#
# pointcloud (included in PGDG, obsolete)
#---------------------------------------------#
pointcloud:
	rm -rf ~/rpmbuild/RPMS/x86_64/pointcloud*.rpm;
	rpmbuild --without debuginfo --define "pgmajorversion 12" -ba ~/rpmbuild/SPECS/pointcloud.spec
	rpmbuild --without debuginfo --define "pgmajorversion 13" -ba ~/rpmbuild/SPECS/pointcloud.spec
	rpmbuild --without debuginfo --define "pgmajorversion 14" -ba ~/rpmbuild/SPECS/pointcloud.spec
	rpmbuild --without debuginfo --define "pgmajorversion 15" -ba ~/rpmbuild/SPECS/pointcloud.spec
	rpmbuild --without debuginfo --define "pgmajorversion 16" -ba ~/rpmbuild/SPECS/pointcloud.spec

#---------------------------------------------#
# imgsmlr
#---------------------------------------------#
imgsmlr:
	rm -rf ~/rpmbuild/RPMS/x86_64/imgsmlr*.rpm;
	rpmbuild --without debuginfo --define "pgmajorversion 12" -ba ~/rpmbuild/SPECS/imgsmlr.spec
	rpmbuild --without debuginfo --define "pgmajorversion 13" -ba ~/rpmbuild/SPECS/imgsmlr.spec
	rpmbuild --without debuginfo --define "pgmajorversion 14" -ba ~/rpmbuild/SPECS/imgsmlr.spec
	rpmbuild --without debuginfo --define "pgmajorversion 15" -ba ~/rpmbuild/SPECS/imgsmlr.spec
	rpmbuild --without debuginfo --define "pgmajorversion 16" -ba ~/rpmbuild/SPECS/imgsmlr.spec

#---------------------------------------------#
# pg_similarity
#---------------------------------------------#
pg_similarity:
	rm -rf ~/rpmbuild/RPMS/x86_64/pg_similarity*.rpm;
	rpmbuild --without debuginfo --define "pgmajorversion 12" -ba ~/rpmbuild/SPECS/pg_similarity.spec
	rpmbuild --without debuginfo --define "pgmajorversion 13" -ba ~/rpmbuild/SPECS/pg_similarity.spec
	rpmbuild --without debuginfo --define "pgmajorversion 14" -ba ~/rpmbuild/SPECS/pg_similarity.spec
	rpmbuild --without debuginfo --define "pgmajorversion 15" -ba ~/rpmbuild/SPECS/pg_similarity.spec
	rpmbuild --without debuginfo --define "pgmajorversion 16" -ba ~/rpmbuild/SPECS/pg_similarity.spec

#---------------------------------------------#
# pg_bigm (included in PGDG, obsolete)
#---------------------------------------------#
pg_bigm:
	rm -rf ~/rpmbuild/RPMS/x86_64/pg_bigm*.rpm;
	rpmbuild --without debuginfo --define "pgmajorversion 12" -ba ~/rpmbuild/SPECS/pg_bigm.spec
	rpmbuild --without debuginfo --define "pgmajorversion 13" -ba ~/rpmbuild/SPECS/pg_bigm.spec
	rpmbuild --without debuginfo --define "pgmajorversion 14" -ba ~/rpmbuild/SPECS/pg_bigm.spec
	rpmbuild --without debuginfo --define "pgmajorversion 15" -ba ~/rpmbuild/SPECS/pg_bigm.spec

#---------------------------------------------#
# hydra (lz4-devel libzstd-devel)
#---------------------------------------------#
hydra:
	rm -rf ~/rpmbuild/RPMS/x86_64/hydra*.rpm;
	PATH=/usr/pgsql-13/bin:/usr/bin/:$PATH rpmbuild --define "pgmajorversion 13" -ba ~/rpmbuild/SPECS/hydra.spec
	PATH=/usr/pgsql-14/bin:/usr/bin/:$PATH rpmbuild --define "pgmajorversion 14" -ba ~/rpmbuild/SPECS/hydra.spec
	PATH=/usr/pgsql-15/bin:/usr/bin/:$PATH rpmbuild --define "pgmajorversion 15" -ba ~/rpmbuild/SPECS/hydra.spec
	PATH=/usr/pgsql-16/bin:/usr/bin/:$PATH rpmbuild --define "pgmajorversion 16" -ba ~/rpmbuild/SPECS/hydra.spec


#---------------------------------------------#
# pg_filedump (lz4-devel libzstd-devel)
#---------------------------------------------#
pg_filedump:
	rm -rf ~/rpmbuild/RPMS/x86_64/pg_filedump*.rpm;
	rpmbuild --define "pgmajorversion 16" -ba ~/rpmbuild/SPECS/pg_filedump.spec

#---------------------------------------------#
# apache-age  (dnf install perl perl-FindBin)
# yum install gcc glibc glib-common readline readline-devel zlib zlib-devel flex bison
#---------------------------------------------#
age:
	rm -rf ~/rpmbuild/RPMS/x86_64/age*.rpm;
	rpmbuild --define "pgmajorversion 16" -ba ~/rpmbuild/SPECS/age16.spec

age15:
	rm -rf ~/rpmbuild/RPMS/x86_64/age*.rpm;
	rpmbuild --define "pgmajorversion 15" -ba ~/rpmbuild/SPECS/age15.spec



#---------------------------------------------#
# duckdb & duckdb_fdw
#---------------------------------------------#
libduckdb:
	rm -rf ~/rpmbuild/RPMS/x86_64/libduckdb*.rpm;
	rpmbuild --without debuginfo -ba ~/rpmbuild/SPECS/libduckdb.spec

# scws is required when building zhparser
libduckdb-install:
	sudo yum remove -y libduckdb || /bin/true
	sudo rpm -ivh ~/rpmbuild/RPMS/x86_64/libduckdb-1.0.0-1PIGSTY.el*.x86_64.rpm

duckdb_fdw:
	rpmbuild --define "pgmajorversion 12" -ba ~/rpmbuild/SPECS/duckdb_fdw.spec
	rpmbuild --define "pgmajorversion 13" -ba ~/rpmbuild/SPECS/duckdb_fdw.spec
	rpmbuild --define "pgmajorversion 14" -ba ~/rpmbuild/SPECS/duckdb_fdw.spec
	rpmbuild --define "pgmajorversion 15" -ba ~/rpmbuild/SPECS/duckdb_fdw.spec
	rpmbuild --define "pgmajorversion 16" -ba ~/rpmbuild/SPECS/duckdb_fdw.spec

#---------------------------------------------#
# pg_tde
#---------------------------------------------#
pg_tde:
	rm -rf ~/rpmbuild/RPMS/x86_64/pg_tde*.rpm;
	rpmbuild --define "pgmajorversion 16" -ba ~/rpmbuild/SPECS/pg_tde.spec

#---------------------------------------------#
# md5hash
#---------------------------------------------#
md5hash:
	rm -rf ~/rpmbuild/RPMS/x86_64/md5hash*.rpm;
	rpmbuild --define "pgmajorversion 12" -ba ~/rpmbuild/SPECS/md5hash.spec
	rpmbuild --define "pgmajorversion 13" -ba ~/rpmbuild/SPECS/md5hash.spec
	rpmbuild --define "pgmajorversion 14" -ba ~/rpmbuild/SPECS/md5hash.spec
	rpmbuild --define "pgmajorversion 15" -ba ~/rpmbuild/SPECS/md5hash.spec
	rpmbuild --define "pgmajorversion 16" -ba ~/rpmbuild/SPECS/md5hash.spec

#---------------------------------------------#
# plv8
#---------------------------------------------#
plv8:
	rm -rf ~/rpmbuild/RPMS/x86_64/plv8*.rpm;
	rpmbuild --define "pgmajorversion 16" -ba ~/rpmbuild/SPECS/plv8.spec
	rpmbuild --define "pgmajorversion 15" -ba ~/rpmbuild/SPECS/plv8.spec
	rpmbuild --define "pgmajorversion 14" -ba ~/rpmbuild/SPECS/plv8.spec
	rpmbuild --define "pgmajorversion 13" -ba ~/rpmbuild/SPECS/plv8.spec
	rpmbuild --define "pgmajorversion 12" -ba ~/rpmbuild/SPECS/plv8.spec

#---------------------------------------------#
# libarrow-s3
#---------------------------------------------#
libarrow-s3:
	rm -rf ~/rpmbuild/RPMS/x86_64/libarrow-s3*.rpm;
	rpmbuild -ba ~/rpmbuild/SPECS/libarrow-s3.spec

#---------------------------------------------#
# parquet_s3_fdw
#---------------------------------------------#
parquet_s3_fdw:
	rm -rf ~/rpmbuild/RPMS/x86_64/parquet_s3_fdw*.rpm;
	rpmbuild --define "pgmajorversion 16" -ba ~/rpmbuild/SPECS/parquet_s3_fdw.spec

#---------------------------------------------#
# pgml [RUST]
#---------------------------------------------#
pgml:
	rm -rf ~/rpmbuild/RPMS/x86_64/pgml*.rpm;
	rpmbuild --without debuginfo --define "pgmajorversion 16" -ba ~/rpmbuild/SPECS/pgml.spec
	rpmbuild --without debuginfo --define "pgmajorversion 15" -ba ~/rpmbuild/SPECS/pgml.spec
	rpmbuild --without debuginfo --define "pgmajorversion 14" -ba ~/rpmbuild/SPECS/pgml.spec

#---------------------------------------------#
# pg_search [RUST]
#---------------------------------------------#
pg_search:
	rm -rf ~/rpmbuild/RPMS/x86_64/pg_search*.rpm;
	rpmbuild --without debuginfo --define "pgmajorversion 16" -ba ~/rpmbuild/SPECS/pg_search.spec
	rpmbuild --without debuginfo --define "pgmajorversion 15" -ba ~/rpmbuild/SPECS/pg_search.spec
	rpmbuild --without debuginfo --define "pgmajorversion 14" -ba ~/rpmbuild/SPECS/pg_search.spec
	rpmbuild --without debuginfo --define "pgmajorversion 13" -ba ~/rpmbuild/SPECS/pg_search.spec
	rpmbuild --without debuginfo --define "pgmajorversion 12" -ba ~/rpmbuild/SPECS/pg_search.spec

#---------------------------------------------#
# pg_lakehouse [RUST]
#---------------------------------------------#
pg_lakehouse:
	rm -rf ~/rpmbuild/RPMS/x86_64/pg_lakehouse*.rpm;
	rpmbuild --without debuginfo --define "pgmajorversion 16" -ba ~/rpmbuild/SPECS/pg_lakehouse.spec
	rpmbuild --without debuginfo --define "pgmajorversion 15" -ba ~/rpmbuild/SPECS/pg_lakehouse.spec

#---------------------------------------------#
# pg_graphql [RUST]
#---------------------------------------------#
pg_graphql:
	rm -rf ~/rpmbuild/RPMS/x86_64/pg_graphql*.rpm;
	rpmbuild --without debuginfo --define "pgmajorversion 16" -ba ~/rpmbuild/SPECS/pg_graphql.spec
	rpmbuild --without debuginfo --define "pgmajorversion 15" -ba ~/rpmbuild/SPECS/pg_graphql.spec
	rpmbuild --without debuginfo --define "pgmajorversion 14" -ba ~/rpmbuild/SPECS/pg_graphql.spec

#---------------------------------------------#
# pg_jsonschema [RUST]
#---------------------------------------------#
pg_jsonschema:
	rm -rf ~/rpmbuild/RPMS/x86_64/pg_jsonschema*.rpm;
	rpmbuild --without debuginfo --define "pgmajorversion 16" -ba ~/rpmbuild/SPECS/pg_jsonschema.spec
	rpmbuild --without debuginfo --define "pgmajorversion 15" -ba ~/rpmbuild/SPECS/pg_jsonschema.spec
	rpmbuild --without debuginfo --define "pgmajorversion 14" -ba ~/rpmbuild/SPECS/pg_jsonschema.spec
	rpmbuild --without debuginfo --define "pgmajorversion 13" -ba ~/rpmbuild/SPECS/pg_jsonschema.spec
	rpmbuild --without debuginfo --define "pgmajorversion 12" -ba ~/rpmbuild/SPECS/pg_jsonschema.spec

#---------------------------------------------#
# wrappers [RUST]
#---------------------------------------------#
wrappers:
	rm -rf ~/rpmbuild/RPMS/x86_64/wrappers*.rpm;
	rpmbuild --without debuginfo --define "pgmajorversion 16" -ba ~/rpmbuild/SPECS/wrappers.spec
	rpmbuild --without debuginfo --define "pgmajorversion 15" -ba ~/rpmbuild/SPECS/wrappers.spec
	rpmbuild --without debuginfo --define "pgmajorversion 14" -ba ~/rpmbuild/SPECS/wrappers.spec

#---------------------------------------------#
# pgmq [RUST]
#---------------------------------------------#
pgmq:
	rm -rf ~/rpmbuild/RPMS/x86_64/pgmq*.rpm;
	rpmbuild --without debuginfo --define "pgmajorversion 16" -ba ~/rpmbuild/SPECS/pgmq.spec
	rpmbuild --without debuginfo --define "pgmajorversion 15" -ba ~/rpmbuild/SPECS/pgmq.spec
	rpmbuild --without debuginfo --define "pgmajorversion 14" -ba ~/rpmbuild/SPECS/pgmq.spec
	rpmbuild --without debuginfo --define "pgmajorversion 13" -ba ~/rpmbuild/SPECS/pgmq.spec
	rpmbuild --without debuginfo --define "pgmajorversion 12" -ba ~/rpmbuild/SPECS/pgmq.spec

#---------------------------------------------#
# pg_tier [RUST]
#---------------------------------------------#
pg_tier:
	rm -rf ~/rpmbuild/RPMS/x86_64/pg_tier*.rpm;
	rpmbuild --without debuginfo --define "pgmajorversion 16" -ba ~/rpmbuild/SPECS/pg_tier.spec

#---------------------------------------------#
# pg_vectorize [RUST]
#---------------------------------------------#
pg_vectorize:
	rm -rf ~/rpmbuild/RPMS/x86_64/pg_vectorize*.rpm;
	rpmbuild --without debuginfo --define "pgmajorversion 16" -ba ~/rpmbuild/SPECS/pg_vectorize.spec
	rpmbuild --without debuginfo --define "pgmajorversion 15" -ba ~/rpmbuild/SPECS/pg_vectorize.spec
	rpmbuild --without debuginfo --define "pgmajorversion 14" -ba ~/rpmbuild/SPECS/pg_vectorize.spec

#---------------------------------------------#
# pg_later [RUST]
#---------------------------------------------#
pg_later:
	rm -rf ~/rpmbuild/RPMS/x86_64/pg_later*.rpm;
	rpmbuild --without debuginfo --define "pgmajorversion 16" -ba ~/rpmbuild/SPECS/pg_later.spec
	rpmbuild --without debuginfo --define "pgmajorversion 15" -ba ~/rpmbuild/SPECS/pg_later.spec
	rpmbuild --without debuginfo --define "pgmajorversion 14" -ba ~/rpmbuild/SPECS/pg_later.spec
	rpmbuild --without debuginfo --define "pgmajorversion 13" -ba ~/rpmbuild/SPECS/pg_later.spec

#---------------------------------------------#
# plprql [RUST]
#---------------------------------------------#
plprql:
	rm -rf ~/rpmbuild/RPMS/x86_64/plprql*.rpm;
	rpmbuild --without debuginfo --define "pgmajorversion 16" -ba ~/rpmbuild/SPECS/plprql.spec
	rpmbuild --without debuginfo --define "pgmajorversion 15" -ba ~/rpmbuild/SPECS/plprql.spec
	rpmbuild --without debuginfo --define "pgmajorversion 14" -ba ~/rpmbuild/SPECS/plprql.spec
	rpmbuild --without debuginfo --define "pgmajorversion 13" -ba ~/rpmbuild/SPECS/plprql.spec
	rpmbuild --without debuginfo --define "pgmajorversion 12" -ba ~/rpmbuild/SPECS/plprql.spec

#---------------------------------------------#
# pg_idkit [RUST]
#---------------------------------------------#
pg_idkit:
	rm -rf ~/rpmbuild/RPMS/x86_64/pg_idkit*.rpm;
	rm -rf ~/rpmbuild/RPMS/x86_64/plprql*.rpm;
	rpmbuild --without debuginfo --define "pgmajorversion 16" -ba ~/rpmbuild/SPECS/pg_idkit.spec
	rpmbuild --without debuginfo --define "pgmajorversion 15" -ba ~/rpmbuild/SPECS/pg_idkit.spec
	rpmbuild --without debuginfo --define "pgmajorversion 14" -ba ~/rpmbuild/SPECS/pg_idkit.spec
	rpmbuild --without debuginfo --define "pgmajorversion 13" -ba ~/rpmbuild/SPECS/pg_idkit.spec
	rpmbuild --without debuginfo --define "pgmajorversion 12" -ba ~/rpmbuild/SPECS/pg_idkit.spec

#---------------------------------------------#
# pgsmcrypto [RUST]
#---------------------------------------------#
pgsmcrypto:
	rm -rf ~/rpmbuild/RPMS/x86_64/pgsmcrypto*.rpm;
	rpmbuild --without debuginfo --define "pgmajorversion 16" -ba ~/rpmbuild/SPECS/pgsmcrypto.spec
	rpmbuild --without debuginfo --define "pgmajorversion 15" -ba ~/rpmbuild/SPECS/pgsmcrypto.spec
	rpmbuild --without debuginfo --define "pgmajorversion 14" -ba ~/rpmbuild/SPECS/pgsmcrypto.spec
	rpmbuild --without debuginfo --define "pgmajorversion 13" -ba ~/rpmbuild/SPECS/pgsmcrypto.spec
	rpmbuild --without debuginfo --define "pgmajorversion 12" -ba ~/rpmbuild/SPECS/pgsmcrypto.spec

#---------------------------------------------#
# pgdd [RUST]
#---------------------------------------------#
pgdd:
	rm -rf ~/rpmbuild/RPMS/x86_64/pgdd*.rpm;
	rpmbuild --without debuginfo --define "pgmajorversion 16" -ba ~/rpmbuild/SPECS/pgdd.spec
	rpmbuild --without debuginfo --define "pgmajorversion 15" -ba ~/rpmbuild/SPECS/pgdd.spec
	rpmbuild --without debuginfo --define "pgmajorversion 14" -ba ~/rpmbuild/SPECS/pgdd.spec
	rpmbuild --without debuginfo --define "pgmajorversion 13" -ba ~/rpmbuild/SPECS/pgdd.spec
	rpmbuild --without debuginfo --define "pgmajorversion 12" -ba ~/rpmbuild/SPECS/pgdd.spec

#---------------------------------------------#
# pg_tiktoken [RUST]
#---------------------------------------------#
pg_tiktoken:
	rm -rf ~/rpmbuild/RPMS/x86_64/pg_tiktoken*.rpm;
	rpmbuild --without debuginfo --define "pgmajorversion 16" -ba ~/rpmbuild/SPECS/pg_tiktoken.spec
	rpmbuild --without debuginfo --define "pgmajorversion 15" -ba ~/rpmbuild/SPECS/pg_tiktoken.spec
	rpmbuild --without debuginfo --define "pgmajorversion 14" -ba ~/rpmbuild/SPECS/pg_tiktoken.spec
	rpmbuild --without debuginfo --define "pgmajorversion 13" -ba ~/rpmbuild/SPECS/pg_tiktoken.spec
	rpmbuild --without debuginfo --define "pgmajorversion 12" -ba ~/rpmbuild/SPECS/pg_tiktoken.spec

#---------------------------------------------#
# pgvectorscale [RUST]
#---------------------------------------------#
pgvectorscale:
	rm -rf ~/rpmbuild/RPMS/x86_64/pgvectorscale*.rpm;
	rpmbuild --without debuginfo --define "pgmajorversion 16" -ba ~/rpmbuild/SPECS/pgvectorscale.spec
	rpmbuild --without debuginfo --define "pgmajorversion 15" -ba ~/rpmbuild/SPECS/pgvectorscale.spec



#---------------------------------------------#
# srpm
#---------------------------------------------#
srpm:
	rpmbuild --define "pgmajorversion 15"  -bs ~/rpmbuild/SPECS/scws.spec
	rpmbuild --define "pgmajorversion 15"  -bs ~/rpmbuild/SPECS/zhparser.spec
	rpmbuild --define "pgmajorversion 15"  -bs ~/rpmbuild/SPECS/pg_embedding.spec
	rpmbuild --define "pgmajorversion 15"  -bs ~/rpmbuild/SPECS/pg_roaringbitmap.spec
	rpmbuild --define "pgmajorversion 15"  -bs ~/rpmbuild/SPECS/pg_tle.spec
	rpmbuild --define "pgmajorversion 15"  -bs ~/rpmbuild/SPECS/pgsql_http.spec
	rpmbuild --define "pgmajorversion 15"  -bs ~/rpmbuild/SPECS/age.spec

ls-srpm:
	ls -alh  ~/rpmbuild/SRPMS/
ls-rpm:
	ls -alh  ~/rpmbuild/RPMS/x86_64/
rm-srpm:
	rm -rf  ~/rpmbuild/SRPMS/*
rm-rpm:
	rm -rf  ~/rpmbuild/RPMS/*

#---------------------------------------------#
# repo build
#---------------------------------------------#
repo7:
	rm -rf /tmp/el7.x86_64; mkdir -p /tmp/el7.x86_64/debug
	cp -r ~/rpmbuild/RPMS/x86_64/* /tmp/el7.x86_64/
	cd /tmp/el7.x86_64/ && mv *debug*.rpm debug/
	cd /tmp/el7.x86_64/ && createrepo_c .
	cd /tmp/el7.x86_64/debug && createrepo_c .
	chmod -R a+r /tmp/el7.x86_64/

repo8:
	rm -rf /tmp/el8.x86_64; mkdir -p /tmp/el8.x86_64/debug
	cp -r ~/rpmbuild/RPMS/x86_64/* /tmp/el8.x86_64/
	cd /tmp/el8.x86_64/ && mv *debug*.rpm debug/
	cd /tmp/el8.x86_64/ && createrepo_c . && repo2module -s stable . modules.yaml && modifyrepo_c --mdtype=modules modules.yaml repodata/
	cd /tmp/el8.x86_64/debug && createrepo_c . && repo2module -s stable . modules.yaml && modifyrepo_c --mdtype=modules modules.yaml repodata/
	chmod -R a+r /tmp/el8.x86_64/

repo9:
	rm -rf /tmp/el9.x86_64; mkdir -p /tmp/el9.x86_64/debug
	cp -r ~/rpmbuild/RPMS/x86_64/* /tmp/el9.x86_64/
	cd /tmp/el9.x86_64/ && mv *debug*.rpm debug/
	cd /tmp/el9.x86_64/ && 	createrepo_c . && repo2module -s stable . modules.yaml && modifyrepo_c --mdtype=modules modules.yaml repodata/
	cd /tmp/el9.x86_64/debug && createrepo_c . && repo2module -s stable . modules.yaml && modifyrepo_c --mdtype=modules modules.yaml repodata/
	chmod -R a+r /tmp/el9.x86_64/



#---------------------------------------------#
# pg_dirtyread (included in PGDG, obsolete)
#---------------------------------------------#
pg_dirtyread:
	rm -rf ~/rpmbuild/RPMS/x86_64/pg_dirtyread*.rpm;
	rpmbuild --define "pgmajorversion 12" -ba ~/rpmbuild/SPECS/pg_dirtyread.spec
	rpmbuild --define "pgmajorversion 13" -ba ~/rpmbuild/SPECS/pg_dirtyread.spec
	rpmbuild --define "pgmajorversion 14" -ba ~/rpmbuild/SPECS/pg_dirtyread.spec
	rpmbuild --define "pgmajorversion 15" -ba ~/rpmbuild/SPECS/pg_dirtyread.spec
	rpmbuild --define "pgmajorversion 16" -ba ~/rpmbuild/SPECS/pg_dirtyread.spec

#---------------------------------------------#
# pg_net (included in PGDG, obsolete)
#---------------------------------------------#
pg_net:
	rm -rf ~/rpmbuild/RPMS/x86_64/pg_net*.rpm;
	rpmbuild --define "pgmajorversion 12" -ba ~/rpmbuild/SPECS/pg_net.spec
	rpmbuild --define "pgmajorversion 13" -ba ~/rpmbuild/SPECS/pg_net.spec
	rpmbuild --define "pgmajorversion 14" -ba ~/rpmbuild/SPECS/pg_net.spec
	rpmbuild --define "pgmajorversion 15" -ba ~/rpmbuild/SPECS/pg_net.spec
	rpmbuild --define "pgmajorversion 16" -ba ~/rpmbuild/SPECS/pg_net.spec

#---------------------------------------------#
# pgsql_http (included in PGDG, obsolete)
#---------------------------------------------#
pgsql_http:
	rm -rf ~/rpmbuild/RPMS/x86_64/pgsql_http*.rpm;
	rpmbuild --define "pgmajorversion 12" -ba ~/rpmbuild/SPECS/pgsql_http.spec
	rpmbuild --define "pgmajorversion 13" -ba ~/rpmbuild/SPECS/pgsql_http.spec
	rpmbuild --define "pgmajorversion 14" -ba ~/rpmbuild/SPECS/pgsql_http.spec
	rpmbuild --define "pgmajorversion 15" -ba ~/rpmbuild/SPECS/pgsql_http.spec
	rpmbuild --define "pgmajorversion 16" -ba ~/rpmbuild/SPECS/pgsql_http.spec

#---------------------------------------------#
# pgsql_gzip (included in PGDG, obsolete)
#---------------------------------------------#
pgsql_gzip:
	rm -rf ~/rpmbuild/RPMS/x86_64/pgsql_gzip*.rpm;
	rpmbuild --define "pgmajorversion 12" -ba ~/rpmbuild/SPECS/pgsql_gzip.spec
	rpmbuild --define "pgmajorversion 13" -ba ~/rpmbuild/SPECS/pgsql_gzip.spec
	rpmbuild --define "pgmajorversion 14" -ba ~/rpmbuild/SPECS/pgsql_gzip.spec
	rpmbuild --define "pgmajorversion 15" -ba ~/rpmbuild/SPECS/pgsql_gzip.spec
	rpmbuild --define "pgmajorversion 16" -ba ~/rpmbuild/SPECS/pgsql_gzip.spec

#---------------------------------------------#
# pg_analytics [RUST] (Obsolete)
#---------------------------------------------#
pg_analytics:
	rm -rf ~/rpmbuild/RPMS/x86_64/pg_analytics*.rpm;
	rpmbuild --without debuginfo --define "pgmajorversion 16" -ba ~/rpmbuild/SPECS/pg_analytics.spec
	rpmbuild --without debuginfo --define "pgmajorversion 15" -ba ~/rpmbuild/SPECS/pg_analytics.spec

#---------------------------------------------#
# phony
#---------------------------------------------#
.PHONY: zhparser zhparser-srpm zhparser-rpm \
		pg_embedding pg_embedding-srpm pg_embedding-rpm \


