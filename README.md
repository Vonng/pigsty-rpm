# PostgreSQL Extensions



| name                                                         | Version                                                      | Version                                                      | Description                | Source       |
| ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ | -------------------------- | ------------ |
| [PostGIS](https://postgis.net/)                              | v3.3.3                                                       | [PostGIS](https://git.osgeo.org/gitea/postgis/postgis/src/branch/master/LICENSE.TXT) (GPLv2+) | 地理空间扩展               | PGDG15       |
| [Citus](https://www.citusdata.com/)                          | v12.0.0                                                      | [AGPLv3](https://github.com/citusdata/citus/blob/main/LICENSE) | 分布式扩展                 | PGDG15       |
| [TimescaleDB](https://www.timescale.com/)                    | v2.11.2                                                      | [Timescale](https://www.timescale.com/legal/licenses/)       | 时序/流计算扩展            | TimescaleDB  |
| [PGVector](https://github.com/pgvector/pgvector)             | v0.5.0                                                       | [PostgreSQL](https://github.com/pgvector/pgvector/blob/master/LICENSE) (BSD-Like) | 向量数据库扩展             | PGDG15       |
| [pg_repack](https://github.com/reorg/pg_repack)              | v1.4.8                                                       | [BSD 3-Clause](https://github.com/reorg/pg_repack/blob/master/COPYRIGHT) | 在线表膨胀治理             | PGDG15       |
| [wal2json](https://github.com/eulerto/wal2json)              | v2.5                                                         | [BSD 3-Clause](https://github.com/eulerto/wal2json/blob/master/LICENSE) | 抽取JSON变更流             | PGDG15       |
| [pglogical](https://github.com/2ndQuadrant/pglogical)        | v2.4.3                                                       | [PostgreSQL](https://github.com/2ndQuadrant/pglogical/blob/REL2_x_STABLE/COPYRIGHT) | 强力逻辑复制               | PGDG15       |
| [pg_cron](https://github.com/citusdata/pg_cron)              | v5.2.1                                                       | [PostgreSQL](https://github.com/citusdata/pg_cron/blob/main/LICENSE) | 库内定时任务               | PGDG15       |
| [passwordcheck_cracklib](https://github.com/devrimgunduz/passwordcheck_cracklib) | v3.0.0                                                       | [LGPLv2.1](https://github.com/devrimgunduz/passwordcheck_cracklib/blob/master/LICENSE) | 强制密码强度               | PGDG15       |
| [zhparser](https://github.com/amutu/zhparser)                | [v2.2](https://github.com/amutu/zhparser/releases/tag/V2.2)  | [PostgreSQL](https://github.com/amutu/zhparser/blob/master/COPYRIGHT) | 中文全文检索               | **PIGSTY**   |
| [pg_embedding](https://github.com/neondatabase/pg_embedding) | [v0.3.6](https://github.com/neondatabase/pg_embedding/archive/refs/tags/0.3.6.tar.gz) | [Apache 2.0](https://github.com/neondatabase/pg_embedding/blob/main/LICENSE) | HNSW向量内存索引           | **PIGSTY**   |
| [roaring_bitmap](https://github.com/ChenHuajun/pg_roaringbitmap) | [v0.5.4](https://github.com/ChenHuajun/pg_roaringbitmap/releases/tag/v0.5.4) | [Apache 2.0](https://github.com/ChenHuajun/pg_roaringbitmap/blob/master/LICENSE) | 高效位图数据类型           | **PIGSTY**   |
| [pg_tle](https://github.com/aws/pg_tle)                      | [1.2.0](https://github.com/aws/pg_tle/releases/tag/v1.2.0)   | [Apache 2.0](https://github.com/aws/pg_tle/blob/main/LICENSE) | 使用可信语言编写/管理扩展  | **PIGSTY**   |
| [Apache AGE](https://github.com/apache/age)                  | [v1.4.0](https://github.com/apache/age/releases/tag/PG15%2Fv1.4.0-rc0) | [Apache 2.0](https://github.com/apache/age/blob/master/LICENSE) | 图数据库扩展               | **PIGSTY**   |
| [pg_net](https://github.com/supabase/pg_net)                 | [0.7.2](https://github.com/supabase/pg_net/releases/tag/v0.7.2) | [Apache 2.0](https://github.com/supabase/pg_net/blob/master/LICENSE) | SQL 接口的异步网络请求     | **PIGSTY**   |
| [pgsql-http](https://github.com/pramsey/pgsql-http)          | [1.6.0](https://github.com/pramsey/pgsql-http/releases/tag/v1.6.0) | [MIT](https://github.com/pramsey/pgsql-http/blob/master/LICENSE.md) | HTTP客户端                 | **PIGSTY**   |
| [pg_hashids](https://github.com/iCyberon/pg_hashids)         | [commit](https://github.com/iCyberon/pg_hashids/commit/83398bcbb616aac2970f5e77d93a3200f0f28e74) | [MIT](https://github.com/iCyberon/pg_hashids/blob/master/LICENSE) | 根据数字生成唯一ID         | ICEBOX       |
| [pgjwt](https://github.com/michelp/pgjwt)                    | [commit](https://github.com/michelp/pgjwt/commit/9742dab1b2f297ad3811120db7b21451bca2d3c9) | [MIT](https://github.com/michelp/pgjwt/blob/master/LICENSE)  | 生成 JWT（JSON Web Token） | ICEBOX       |
| [pg-safeupdate](https://github.com/eradman/pg-safeupdate)    | [1.4](https://github.com/eradman/pg-safeupdate/releases/tag/1.4) | [ISC-Style](https://github.com/eradman/pg-safeupdate/blob/master/LICENSE) | 避免误删/更新数据          | ICEBOX       |
| [pg_plan_filter](https://github.com/pgexperts/pg_plan_filter) | latest                                                       | [PostgreSQL](https://github.com/pgexperts/pg_plan_filter/blob/master/License) | 阻止高开销请求             | ICEBOX       |
| [pg_hint_plan](https://github.com/ossc-db/pg_hint_plan)      | v1.6.0                                                       | Broken                                                       |                            | ICEBOX       |
| [orioledb](https://github.com/orioledb/orioledb)             | beta2                                                        | Broken                                                       |                            | ICEBOX       |
| orafce                                                       |                                                              |                                                              |                            | PGDG15       |
| mysqlcompat                                                  |                                                              |                                                              |                            | PGDG15       |
| mongo_fdw                                                    |                                                              |                                                              |                            | PGDG15       |
| tds_fdw                                                      |                                                              |                                                              |                            | PGDG15       |
| mysql_fdw                                                    |                                                              |                                                              |                            | PGDG15       |
| hdfs_fdw                                                     |                                                              |                                                              |                            | PGDG15       |
| sqlite_fdw                                                   |                                                              |                                                              |                            | PGDG15       |
| pgbouncer_fdw                                                |                                                              |                                                              |                            | PGDG15       |
| multicorn2                                                   |                                                              |                                                              |                            | PGDG15       |
| powa                                                         |                                                              |                                                              |                            | PGDG15       |
| pg_stat_kcache                                               |                                                              |                                                              |                            | PGDG15       |
| pg_stat_monitor                                              |                                                              |                                                              |                            | PGDG15       |
| pg_qualstats                                                 |                                                              |                                                              |                            | PGDG15       |
| pg_track_settings                                            |                                                              |                                                              |                            | PGDG15       |
| pg_wait_sampling                                             |                                                              |                                                              |                            | PGDG15       |
| system_stats                                                 |                                                              |                                                              |                            | PGDG15       |
| plprofiler                                                   |                                                              |                                                              |                            | PGDG15       |
| plproxy                                                      |                                                              |                                                              |                            | PGDG15       |
| plsh                                                         |                                                              |                                                              |                            | PGDG15       |
| pldebugger                                                   |                                                              |                                                              |                            | PGDG15       |
| plpgsql_check                                                |                                                              |                                                              |                            | PGDG15       |
| pgtt                                                         |                                                              |                                                              |                            | PGDG15       |
| pgq                                                          |                                                              |                                                              |                            | PGDG15       |
| pgsql_tweaks                                                 |                                                              |                                                              |                            | PGDG15       |
| count_distinct                                               |                                                              |                                                              |                            | PGDG15       |
| hypopg                                                       |                                                              |                                                              |                            | PGDG15       |
| timestamp9                                                   |                                                              |                                                              |                            | PGDG15       |
| semver                                                       |                                                              |                                                              |                            | PGDG15       |
| prefix                                                       |                                                              |                                                              |                            | PGDG15       |
| rum                                                          |                                                              |                                                              |                            | PGDG15       |
| geoip                                                        |                                                              |                                                              |                            | PGDG15       |
| periods                                                      |                                                              |                                                              |                            | PGDG15       |
| ip4r                                                         |                                                              |                                                              |                            | PGDG15       |
| tdigest                                                      |                                                              |                                                              |                            | PGDG15       |
| hll                                                          |                                                              |                                                              |                            | PGDG15       |
| pgmp                                                         |                                                              |                                                              |                            | PGDG15       |
| extra_window_functions                                       |                                                              |                                                              |                            | PGDG15       |
| topn                                                         |                                                              |                                                              |                            | PGDG15       |
| pg_background                                                |                                                              |                                                              |                            | PGDG15       |
| e-maj                                                        |                                                              |                                                              |                            | PGDG15       |
| pg_catcheck                                                  |                                                              |                                                              |                            | PGDG15       |
| pg_prioritize                                                |                                                              |                                                              |                            | PGDG15       |
| pgcopydb                                                     |                                                              |                                                              |                            | PGDG15       |
| pg_filedump                                                  |                                                              |                                                              |                            | PGDG15       |
| pgcryptokey                                                  |                                                              |                                                              |                            | PGDG15       |
| logerrors                                                    |                                                              |                                                              |                            | PGDG15       |
| pg_top                                                       |                                                              |                                                              |                            | PGDG15       |
| pg_comparator                                                |                                                              |                                                              |                            | PGDG15       |
| pg_ivm                                                       |                                                              |                                                              |                            | PGDG15       |
| pgsodium                                                     |                                                              |                                                              |                            | PGDG15       |
| pgfincore                                                    |                                                              |                                                              |                            | PGDG15       |
| ddlx                                                         |                                                              |                                                              |                            | PGDG15       |
| credcheck                                                    |                                                              |                                                              |                            | PGDG15       |
| safeupdate                                                   |                                                              |                                                              |                            | PGDG15       |
| pg_squeeze                                                   |                                                              |                                                              |                            | PGDG15       |
| pg_fkpart                                                    |                                                              |                                                              |                            | PGDG15       |
| pg_jobmon                                                    |                                                              |                                                              |                            | PGDG15       |
| bgw_replstatus                                               |                                                              |                                                              |                            | PGDG15 / TBD |
| ddlx                                                         |                                                              |                                                              |                            | PGDG15 / TBD |
| geoip                                                        |                                                              |                                                              |                            | PGDG15 / TBD |
| mysqlcompat                                                  |                                                              |                                                              |                            | PGDG15 / TBD |
| pg_auth_mon                                                  |                                                              |                                                              |                            | PGDG15 / TBD |
| pg_auto_failover                                             |                                                              |                                                              |                            | PGDG15 / TBD |
| pg_checksums                                                 |                                                              |                                                              |                            | PGDG15 / TBD |
| pg_dbms_job                                                  |                                                              |                                                              |                            | PGDG15 / TBD |
| pg_failover_slots                                            |                                                              |                                                              |                            | PGDG15 / TBD |
| pg_fkpart                                                    |                                                              |                                                              |                            | PGDG15 / TBD |
| pg_jobmon                                                    |                                                              |                                                              |                            | PGDG15 / TBD |
| pg_partman                                                   |                                                              |                                                              |                            | PGDG15 / TBD |
| pg_permissions                                               |                                                              |                                                              |                            | PGDG15 / TBD |
| pg_readonly                                                  |                                                              |                                                              |                            | PGDG15 / TBD |
| pg_statement_rollback                                        |                                                              |                                                              |                            | PGDG15 / TBD |
| pg_store_plans                                               |                                                              |                                                              |                            | PGDG15 / TBD |
| pg_uuidv7                                                    |                                                              |                                                              |                            | PGDG15 / TBD |
| pgaudit17                                                    |                                                              |                                                              |                            | PGDG15 / TBD |
| pgauditlogtofile                                             |                                                              |                                                              |                            | PGDG15 / TBD |
| pgcopydb                                                     |                                                              |                                                              |                            | PGDG15 / TBD |
| pgsql_tweaks                                                 |                                                              |                                                              |                            | PGDG15 / TBD |
| plprofiler-client                                            |                                                              |                                                              |                            | PGDG15 / TBD |
| plprofiler-server                                            |                                                              |                                                              |                            | PGDG15 / TBD |
| postgresql-unit                                              |                                                              |                                                              |                            | PGDG15 / TBD |
| postgresql_anonymizer                                        |                                                              |                                                              |                            | PGDG15 / TBD |
| postgresql_faker                                             |                                                              |                                                              |                            | PGDG15 / TBD |
| powa-web                                                     |                                                              |                                                              |                            | PGDG15 / TBD |
| set_user                                                     |                                                              |                                                              |                            | PGDG15 / TBD |
| pgagent                                                      |                                                              |                                                              |                            | PGDG15 / TBD |
| [pgTAP](https://pgtap.org/)                                  | [v1.2.0](https://github.com/theory/pgtap/releases/tag/v1.2.0) |                                                              | PG单元测试框架             | SUPA / TBD   |
| [pgAudit](https://www.pgaudit.org/)                          | [1.7.0](https://github.com/pgaudit/pgaudit/releases/tag/1.7.0) |                                                              | 生成合规的审计日志         | SUPA / TBD   |



### Excluded

These extensions are not included in the repository for some reason:

- pgrouting: troubles rpm dependencies, you can add it manually
- plr_15: the entire R stack is too large to be included in the repository
- pl/java: the entire java stack is too heavy to be included in the repository
- pl/v8: the entire javascript stack is too heavy to be included in the repository
- pgexportdoc_15
- pgimportdoc_15
- pgmemcache_15
- pgTAP
- pgAudit?
- 





PG 15: https://download.postgresql.org/pub/repos/yum/srpms/15/redhat/rhel-7-x86_64/






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

Compile
