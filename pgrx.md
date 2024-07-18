# pgrx extension

Here are some extensions build upon the rust library [`pgrx`](https://github.com/pgcentralfoundation/pgrx)

Check dependent packages on [Insight - Dependency graph - Dependents](https://github.com/pgcentralfoundation/pgrx/network/dependents)

## Rust Extensions

Check [`pgrx`](pgrx.md) for RUST extensions

| Vendor        | Name                                                                       | Version | PGRX                                                                                            | License                                                                     | PG Ver         | Deps                 |
|---------------|----------------------------------------------------------------------------|---------|-------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------|----------------|----------------------|
| PostgresML    | [pgml](https://github.com/postgresml/postgresml)                           | v2.9.1  | [v0.11.3](https://github.com/postgresml/postgresml/blob/master/pgml-extension/Cargo.lock#L1785) | [MIT](https://github.com/postgresml/postgresml/blob/master/MIT-LICENSE.txt) | 16,15,14       |                      |
| ParadeDB      | [pg_search](https://github.com/paradedb/paradedb/tree/dev/pg_search)       | v0.8.0  | [v0.11.3](https://github.com/paradedb/paradedb/blob/dev/pg_search/Cargo.toml#L36)               | [AGPLv3](https://github.com/paradedb/paradedb/blob/dev/LICENSE)             | 16,15          |                      |
| ParadeDB      | [pg_lakehouse](https://github.com/paradedb/paradedb/tree/dev/pg_lakehouse) | v0.8.0  | v0.11.3                                                                                         | [AGPLv3](https://github.com/paradedb/paradedb/blob/dev/LICENSE)             | 16,15          |                      |
| Supabase      | [pg_graphql](https://github.com/supabase/pg_graphql)                       | v1.5.6  | [v0.11.3](https://github.com/supabase/pg_graphql/blob/master/Cargo.toml#L17)                    | [Apache-2.0](https://github.com/supabase/pg_graphql/blob/master/LICENSE)    | 16,15          |                      |
| Supabase      | [pg_jsonschema](https://github.com/supabase/pg_jsonschema)                 | v0.3.1  | v0.11.3                                                                                         | [Apache-2.0](https://github.com/supabase/pg_jsonschema/blob/master/LICENSE) | 16,15,14,13,12 |                      |
| Supabase      | [wrappers](https://github.com/supabase/wrappers)                           | v0.4.1  | v0.11.3                                                                                         | [Apache-2.0](https://github.com/supabase/wrappers/blob/main/LICENSE)        | 16,15,14       |                      |
| Tembo         | [pgmq](https://github.com/tembo-io/pgmq)                                   | v1.2.1  | v0.11.3                                                                                         | [PostgreSQL](https://github.com/tembo-io/pgmq)                              | 16,15,14,13,12 |                      |
| Tembo         | [pg_tier](https://github.com/tembo-io/pg_tier)                             | v0.0.4  | v0.11.3                                                                                         | [Apache-2.0](https://github.com/tembo-io/pg_tier/blob/main/LICENSE)         | 16             | pgmq, parquet_s3_fdw |
| Tembo         | [pg_vectorize](https://github.com/tembo-io/pg_vectorize)                   | v0.16.0 | v0.11.3                                                                                         | [PostgreSQL](https://github.com/tembo-io/pg_vectorize/blob/main/LICENSE)    | 16,15,14       | pgmq, pg_cron        |
| Tembo         | [pg_later](https://github.com/tembo-io/pg_later)                           | v0.1.1  | v0.11.3                                                                                         | [PostgreSQL](https://github.com/tembo-io/pg_later/blob/main/LICENSE)        | 16,15,14,13    | pgmq                 |
| VADOSWARE     | [pg_idkit](https://github.com/VADOSWARE/pg_idkit)                          | v0.2.3  | v0.11.3                                                                                         | [Apache-2.0](https://github.com/VADOSWARE/pg_idkit/blob/main/LICENSE)       | 16,15,14,13,12 |                      |
| pgsmcrypto    | [pgsmcrypto](https://github.com/zhuobie/pgsmcrypto)                        | v0.1.0  | v0.11.3                                                                                         | [MIT](https://github.com/zhuobie/pgsmcrypto/blob/main/LICENSE)              | 16,15,14,13,12 |                      |
| kelvich       | [pg_tiktoken](https://github.com/kelvich/pg_tiktoken)                      | v0.0.1  | v0.10.2                                                                                         | [Apache-2.0](https://github.com/kelvich/pg_tiktoken/blob/main/LICENSE)      | 16,15,14,13,12 |                      |
| rustprooflabs | [pgdd](https://github.com/rustprooflabs/pgdd)                              | v0.5.2  | v0.10.2                                                                                         | [MIT](https://github.com/zhuobie/pgsmcrypto/blob/main/LICENSE)              | 16,15,14,13,12 |                      |
| timescale     | [vectorscale](https://github.com/timescale/pgvectorscale)                  | v0.2.0  | v0.11.4                                                                                         | [PostgreSQL](https://github.com/timescale/pgvectorscale/blob/main/LICENSE)  | 16,15,14,13,12 |                      |
| kaspermarstal | [plprql](https://github.com/kaspermarstal/plprql)                          | v0.1.0  | v0.11.4                                                                                         | [Apache-2.0](https://github.com/kaspermarstal/plprql/blob/main/LICENSE)     | 16,15,14,13,12 |                      |

Obsolete extension:

| Vendor        | Name                                                                       | Version | PGRX           | License                                                                     | PG Ver         | Deps                 |
|---------------|----------------------------------------------------------------------------|---------|----------------|-----------------------------------------------------------------------------|----------------|----------------------|
| ParadeDB      | [pg_analytics](https://github.com/paradedb/pg_analytics)                   | v0.6.1  | v0.12.0-alpha0 | [AGPLv3](https://github.com/paradedb/paradedb/blob/dev/LICENSE)             | 16,15          |                      |


----------

## Provision

```bash
make rpm      # use the vagrant rpm spec, add upstream 
./node.yml -i files/pigsty/rpmbuild.yml -t node_repo,node_pkg

# manual install on el8:
sudo yum groupinstall --skip-broken -y 'Development Tools';    # skip broken on EL8 

# create dev structure
rpmdev-setuptreepm
```

----------

## Prepare 

Setup rust & pgrx

```bash
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
source "$HOME/.cargo/env"
```

<details>

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

</details>

YOU **MUST** Pass `HTTPS_PROXY` as following:

```bash
HTTPS_PROXY=http://192.168.0.104:8118 cargo install --locked cargo-pgrx@0.11.3
HTTPS_PROXY=http://192.168.0.104:8118 cargo pgrx init
```



--------

## Build

```bash
cd ~;
cd ~; git clone --recursive git@github.com:postgresml/postgresml.git  ; cd ~/postgresml     && git checkout v2.9.1                 
cd ~; git clone --recursive https://github.com/paradedb/paradedb.git  ; cd ~/paradedb       && git checkout v0.8.4
cd ~; git clone git@github.com:supabase/pg_graphql.git                ; cd ~/pg_graphql     && git checkout v1.5.7                 
cd ~; git clone git@github.com:supabase/pg_jsonschema.git             ; cd ~/pg_jsonschema  && git checkout v0.3.1                    
cd ~; git clone git@github.com:supabase/wrappers.git                  ; cd ~/wrappers       && git checkout v0.3.1               
cd ~; git clone git@github.com:tembo-io/pgmq.git                      ; cd ~/pgmq           && git checkout v1.2.1 #v1.3.3           
cd ~; git clone git@github.com:tembo-io/pg_tier.git                   ; cd ~/pg_tier        && git checkout v0.0.4              
cd ~; git clone git@github.com:tembo-io/pg_vectorize.git              ; cd ~/pg_vectorize   && git checkout v0.16.0                   
cd ~; git clone git@github.com:tembo-io/pg_later.git                  ; cd ~/pg_later       && git checkout v0.1.1               
cd ~; git clone git@github.com:VADOSWARE/pg_idkit.git                 ; cd ~/pg_idkit       && git checkout v0.2.3               
cd ~; git clone git@github.com:zhuobie/pgsmcrypto.git                 ; #cd ~/pgsmcrypto     && git checkout v0.1.0                 
cd ~; git clone git@github.com:kelvich/pg_tiktoken.git                ; #cd ~/pg_tiktoken    && git checkout v1.0.0                  
cd ~; git clone git@github.com:rustprooflabs/pgdd.git                 ; cd ~/pgdd           && git checkout 0.5.2           
cd ~; git clone git@github.com:kaspermarstal/plprql.git               ; cd ~/plprql         && git checkout v0.1.0             
cd ~; git clone git@github.com:timescale/pgvectorscale.git            ; cd ~/pgvectorscale  && git checkout 0.2.0                    

cd ~/paradedb;     HTTPS_PROXY=http://192.168.0.104:8118 cargo update
cd ~/pgmq/pgmq-rs; HTTPS_PROXY=http://192.168.0.104:8118 cargo update
```



| Vendor        | Name                                                                       | Version | PGRX                                                                                            | License                                                                     | PG Ver         | Deps                 |
|---------------|----------------------------------------------------------------------------|---------|-------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------|----------------|----------------------|
| PostgresML    | [pgml](https://github.com/postgresml/postgresml)                           | v2.9.1  | [v0.11.3](https://github.com/postgresml/postgresml/blob/master/pgml-extension/Cargo.lock#L1785) | [MIT](https://github.com/postgresml/postgresml/blob/master/MIT-LICENSE.txt) | 16,15,14       |                      |
| ParadeDB      | [pg_search](https://github.com/paradedb/paradedb/tree/dev/pg_search)       | v0.8.1  | [v0.11.3](https://github.com/paradedb/paradedb/blob/dev/pg_search/Cargo.toml#L36)               | [AGPLv3](https://github.com/paradedb/paradedb/blob/dev/LICENSE)             | 16,15          |                      |
| ParadeDB      | [pg_lakehouse](https://github.com/paradedb/paradedb/tree/dev/pg_lakehouse) | v0.8.1  | v0.11.3                                                                                         | [AGPLv3](https://github.com/paradedb/paradedb/blob/dev/LICENSE)             | 16,15          |                      |
| Supabase      | [pg_graphql](https://github.com/supabase/pg_graphql)                       | v1.5.6  | [v0.11.3](https://github.com/supabase/pg_graphql/blob/master/Cargo.toml#L17)                    | [Apache-2.0](https://github.com/supabase/pg_graphql/blob/master/LICENSE)    | 16,15          |                      |
| Supabase      | [pg_jsonschema](https://github.com/supabase/pg_jsonschema)                 | v0.3.1  | v0.11.3                                                                                         | [Apache-2.0](https://github.com/supabase/pg_jsonschema/blob/master/LICENSE) | 16,15,14,13,12 |                      |
| Supabase      | [wrappers](https://github.com/supabase/wrappers)                           | v0.3.1  | v0.11.3                                                                                         | [Apache-2.0](https://github.com/supabase/wrappers/blob/main/LICENSE)        | 16,15,14       |                      |
| Tembo         | [pgmq](https://github.com/tembo-io/pgmq)                                   | v1.2.1  | v0.11.3                                                                                         | [PostgreSQL](https://github.com/tembo-io/pgmq)                              | 16,15,14,13,12 |                      |
| Tembo         | [pg_tier](https://github.com/tembo-io/pg_tier)                             | v0.0.4  | v0.11.3                                                                                         | [Apache-2.0](https://github.com/tembo-io/pg_tier/blob/main/LICENSE)         | 16             | pgmq, parquet_s3_fdw |
| Tembo         | [pg_vectorize](https://github.com/tembo-io/pg_vectorize)                   | v0.17.0 | v0.11.3                                                                                         | [PostgreSQL](https://github.com/tembo-io/pg_vectorize/blob/main/LICENSE)    | 16,15,14       | pgmq, pg_cron        |
| Tembo         | [pg_later](https://github.com/tembo-io/pg_later)                           | v0.1.1  | v0.11.3                                                                                         | [PostgreSQL](https://github.com/tembo-io/pg_later/blob/main/LICENSE)        | 16,15,14,13    | pgmq                 |
| VADOSWARE     | [pg_idkit](https://github.com/VADOSWARE/pg_idkit)                          | v0.2.3  | v0.11.3                                                                                         | [Apache-2.0](https://github.com/VADOSWARE/pg_idkit/blob/main/LICENSE)       | 16,15,14,13,12 |                      |
| pgsmcrypto    | [pgsmcrypto](https://github.com/zhuobie/pgsmcrypto)                        | v0.1.0  | v0.11.3                                                                                         | [MIT](https://github.com/zhuobie/pgsmcrypto/blob/main/LICENSE)              | 16,15,14,13,12 |                      |
| kelvich       | [pg_tiktoken](https://github.com/kelvich/pg_tiktoken)                      | v0.0.1  | v0.10.2                                                                                         | [Apache-2.0](https://github.com/kelvich/pg_tiktoken/blob/main/LICENSE)      | 16,15,14,13,12 |                      |
| rustprooflabs | [pgdd](https://github.com/rustprooflabs/pgdd)                              | v0.5.2  | v0.10.2                                                                                         | [MIT](https://github.com/zhuobie/pgsmcrypto/blob/main/LICENSE)              | 16,15,14,13,12 |                      |
| timescale     | [vectorscale](https://github.com/timescale/pgvectorscale)                  | v0.2.0  | v0.11.4                                                                                         | [PostgreSQL](https://github.com/timescale/pgvectorscale/blob/main/LICENSE)  | 16,15,14,13,12 |                      |
| kaspermarstal | [plprql](https://github.com/kaspermarstal/plprql)                          | v0.1.0  | v0.11.4                                                                                         | [Apache-2.0](https://github.com/kaspermarstal/plprql/blob/main/LICENSE)     | 16,15,14,13,12 |                      |



```bash
alias pg16="export PATH=/usr/pgsql-16/bin:/root/.cargo/bin:/pg/bin:/usr/share/Modules/bin:/usr/lib64/ccache:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/root/bin:/home/vagrant/.cargo/bin;"
alias pg15="export PATH=/usr/pgsql-15/bin:/root/.cargo/bin:/pg/bin:/usr/share/Modules/bin:/usr/lib64/ccache:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/root/bin:/home/vagrant/.cargo/bin;"
alias pg14="export PATH=/usr/pgsql-14/bin:/root/.cargo/bin:/pg/bin:/usr/share/Modules/bin:/usr/lib64/ccache:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/root/bin:/home/vagrant/.cargo/bin;"
alias pg13="export PATH=/usr/pgsql-13/bin:/root/.cargo/bin:/pg/bin:/usr/share/Modules/bin:/usr/lib64/ccache:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/root/bin:/home/vagrant/.cargo/bin;"
alias pg12="export PATH=/usr/pgsql-12/bin:/root/.cargo/bin:/pg/bin:/usr/share/Modules/bin:/usr/lib64/ccache:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/root/bin:/home/vagrant/.cargo/bin;"
alias bd="HTTPS_PROXY=http://192.168.0.104:8118 cargo pgrx package  -v"


```


```bash
alias pg16="export PATH=/usr/lib/postgresql/16/bin:/home/vagrant/.cargo/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/snap/bin;"
alias pg15="export PATH=/usr/lib/postgresql/15/bin:/home/vagrant/.cargo/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/snap/bin;"
alias pg14="export PATH=/usr/lib/postgresql/14/bin:/home/vagrant/.cargo/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/snap/bin;"
alias pg13="export PATH=/usr/lib/postgresql/13/bin:/home/vagrant/.cargo/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/snap/bin;"
alias pg12="export PATH=/usr/lib/postgresql/12/bin:/home/vagrant/.cargo/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/snap/bin;"
alias build="HTTPS_PROXY=http://192.168.0.104:8118 cargo pgrx package -v"


# pgrx 0.11.3
cd ~/paradedb/pg_search;       HTTPS_PROXY=http://192.168.0.104:8118 cargo pgrx package  -v;   # 16,15
cd ~/paradedb/pg_lakehouse;    HTTPS_PROXY=http://192.168.0.104:8118 cargo pgrx package  -v;   # 16,15
cd ~/pg_graphql;               HTTPS_PROXY=http://192.168.0.104:8118 cargo pgrx package  -v;   # 16,15,14
cd ~/pg_jsonschema;            HTTPS_PROXY=http://192.168.0.104:8118 cargo pgrx package  -v;   # 16,15,14,13,12
cd ~/wrappers/wrappers;        HTTPS_PROXY=http://192.168.0.104:8118 cargo pgrx package  -v;   # 16,15,14

cd ~/pgmq;                     HTTPS_PROXY=http://192.168.0.104:8118 cargo pgrx package  -v;   # 16,15,14,13,12
cd ~/pg_tier;                  HTTPS_PROXY=http://192.168.0.104:8118 cargo pgrx package  -v;   # 16
cd ~/pg_vectorize/extension;   HTTPS_PROXY=http://192.168.0.104:8118 cargo pgrx package  -v;   # 16,15,14
cd ~/pg_later;                 HTTPS_PROXY=http://192.168.0.104:8118 cargo pgrx package  -v;   # 16,15,14,13

cd ~/pgsmcrypto;               HTTPS_PROXY=http://192.168.0.104:8118 cargo pgrx package  -v;   # 16,15,14,13,12
cd ~/pg_idkit;                 HTTPS_PROXY=http://192.168.0.104:8118 cargo pgrx package  -v;   # 16,15,14,13,12

cd ~/plprql/plprql;              HTTPS_PROXY=http://192.168.0.104:8118 cargo pgrx package  -v; # 16,15,14,13,12

export RUSTFLAGS="-C target-feature=+avx2,+fma"
cd ~/pgvectorscale/pgvectorscale HTTPS_PROXY=http://192.168.0.104:8118 cargo pgrx package  -v; # 16,15

# pgrx 0.10.2
cd ~/pgdd;                     HTTPS_PROXY=http://192.168.0.104:8118 cargo pgrx package  -v;   # 16,15,14
cd ~/pg_tiktoken;              HTTPS_PROXY=http://192.168.0.104:8118 cargo pgrx package  -v;   # 16,15,14
```


## Package

How to package Rust extensions for PostgreSQL

```bash
rm -rf ~/rpmbuild/SOURCES/pgml_16; cp -r ~/postgresml/pgml-extension/target/release/pgml-pg16 ~/rpmbuild/SOURCES/pgml_16;
rm -rf ~/rpmbuild/SOURCES/pgml_15; cp -r ~/postgresml/pgml-extension/target/release/pgml-pg15 ~/rpmbuild/SOURCES/pgml_15;
rm -rf ~/rpmbuild/SOURCES/pgml_14; cp -r ~/postgresml/pgml-extension/target/release/pgml-pg14 ~/rpmbuild/SOURCES/pgml_14;

rm -rf ~/rpmbuild/SOURCES/pg_search_16;     cp -r ~/paradedb/target/release/pg_search-pg16      ~/rpmbuild/SOURCES/pg_search_16;
rm -rf ~/rpmbuild/SOURCES/pg_search_15;     cp -r ~/paradedb/target/release/pg_search-pg15      ~/rpmbuild/SOURCES/pg_search_15;
rm -rf ~/rpmbuild/SOURCES/pg_search_14;     cp -r ~/paradedb/target/release/pg_search-pg14      ~/rpmbuild/SOURCES/pg_search_14;
rm -rf ~/rpmbuild/SOURCES/pg_search_13;     cp -r ~/paradedb/target/release/pg_search-pg13      ~/rpmbuild/SOURCES/pg_search_13;
rm -rf ~/rpmbuild/SOURCES/pg_search_12;     cp -r ~/paradedb/target/release/pg_search-pg12      ~/rpmbuild/SOURCES/pg_search_12;

rm -rf ~/rpmbuild/SOURCES/pg_lakehouse_16;  cp -r ~/paradedb/target/release/pg_lakehouse-pg16   ~/rpmbuild/SOURCES/pg_lakehouse_16;
rm -rf ~/rpmbuild/SOURCES/pg_lakehouse_15;  cp -r ~/paradedb/target/release/pg_lakehouse-pg15   ~/rpmbuild/SOURCES/pg_lakehouse_15;

rm -rf ~/rpmbuild/SOURCES/pg_graphql_16;    cp -r ~/pg_graphql/target/release/pg_graphql-pg16 ~/rpmbuild/SOURCES/pg_graphql_16;
rm -rf ~/rpmbuild/SOURCES/pg_graphql_15;    cp -r ~/pg_graphql/target/release/pg_graphql-pg15 ~/rpmbuild/SOURCES/pg_graphql_15;
rm -rf ~/rpmbuild/SOURCES/pg_graphql_14;    cp -r ~/pg_graphql/target/release/pg_graphql-pg14 ~/rpmbuild/SOURCES/pg_graphql_14;

rm -rf ~/rpmbuild/SOURCES/pg_jsonschema_16; cp -r ~/pg_jsonschema/target/release/pg_jsonschema-pg16 ~/rpmbuild/SOURCES/pg_jsonschema_16;
rm -rf ~/rpmbuild/SOURCES/pg_jsonschema_15; cp -r ~/pg_jsonschema/target/release/pg_jsonschema-pg15 ~/rpmbuild/SOURCES/pg_jsonschema_15;
rm -rf ~/rpmbuild/SOURCES/pg_jsonschema_14; cp -r ~/pg_jsonschema/target/release/pg_jsonschema-pg14 ~/rpmbuild/SOURCES/pg_jsonschema_14;
rm -rf ~/rpmbuild/SOURCES/pg_jsonschema_13; cp -r ~/pg_jsonschema/target/release/pg_jsonschema-pg13 ~/rpmbuild/SOURCES/pg_jsonschema_13;
rm -rf ~/rpmbuild/SOURCES/pg_jsonschema_12; cp -r ~/pg_jsonschema/target/release/pg_jsonschema-pg12 ~/rpmbuild/SOURCES/pg_jsonschema_12;

rm -rf ~/rpmbuild/SOURCES/wrappers_16;      cp -r ~/wrappers/target/release/wrappers-pg16 ~/rpmbuild/SOURCES/wrappers_16;
rm -rf ~/rpmbuild/SOURCES/wrappers_15;      cp -r ~/wrappers/target/release/wrappers-pg15 ~/rpmbuild/SOURCES/wrappers_15;
rm -rf ~/rpmbuild/SOURCES/wrappers_14;      cp -r ~/wrappers/target/release/wrappers-pg14 ~/rpmbuild/SOURCES/wrappers_14;

rm -rf ~/rpmbuild/SOURCES/pgmq_16;          cp -r ~/pgmq/target/release/pgmq-pg16 ~/rpmbuild/SOURCES/pgmq_16;
rm -rf ~/rpmbuild/SOURCES/pgmq_15;          cp -r ~/pgmq/target/release/pgmq-pg15 ~/rpmbuild/SOURCES/pgmq_15;
rm -rf ~/rpmbuild/SOURCES/pgmq_14;          cp -r ~/pgmq/target/release/pgmq-pg14 ~/rpmbuild/SOURCES/pgmq_14;
rm -rf ~/rpmbuild/SOURCES/pgmq_13;          cp -r ~/pgmq/target/release/pgmq-pg13 ~/rpmbuild/SOURCES/pgmq_13;
rm -rf ~/rpmbuild/SOURCES/pgmq_12;          cp -r ~/pgmq/target/release/pgmq-pg12 ~/rpmbuild/SOURCES/pgmq_12;

rm -rf ~/rpmbuild/SOURCES/pg_later_16;      cp -r ~/pg_later/target/release/pg_later-pg16 ~/rpmbuild/SOURCES/pg_later_16;
rm -rf ~/rpmbuild/SOURCES/pg_later_15;      cp -r ~/pg_later/target/release/pg_later-pg15 ~/rpmbuild/SOURCES/pg_later_15;
rm -rf ~/rpmbuild/SOURCES/pg_later_14;      cp -r ~/pg_later/target/release/pg_later-pg14 ~/rpmbuild/SOURCES/pg_later_14;
rm -rf ~/rpmbuild/SOURCES/pg_later_13;      cp -r ~/pg_later/target/release/pg_later-pg13 ~/rpmbuild/SOURCES/pg_later_13;

rm -rf ~/rpmbuild/SOURCES/vectorize_16;     cp -r ~/pg_vectorize/extension/target/release/vectorize-pg16 ~/rpmbuild/SOURCES/vectorize_16;
rm -rf ~/rpmbuild/SOURCES/vectorize_15;     cp -r ~/pg_vectorize/extension/target/release/vectorize-pg15 ~/rpmbuild/SOURCES/vectorize_15;
rm -rf ~/rpmbuild/SOURCES/vectorize_14;     cp -r ~/pg_vectorize/extension/target/release/vectorize-pg14 ~/rpmbuild/SOURCES/vectorize_14;

rm -rf ~/rpmbuild/SOURCES/pg_tier_16;       cp -r ~/pg_tier/target/release/pg_tier-pg16 ~/rpmbuild/SOURCES/pg_tier_16;

rm -rf ~/rpmbuild/SOURCES/pg_idkit_16;      cp -r ~/pg_idkit/target/release/pg_idkit-pg16 ~/rpmbuild/SOURCES/pg_idkit_16;
rm -rf ~/rpmbuild/SOURCES/pg_idkit_15;      cp -r ~/pg_idkit/target/release/pg_idkit-pg15 ~/rpmbuild/SOURCES/pg_idkit_15;
rm -rf ~/rpmbuild/SOURCES/pg_idkit_14;      cp -r ~/pg_idkit/target/release/pg_idkit-pg14 ~/rpmbuild/SOURCES/pg_idkit_14;
rm -rf ~/rpmbuild/SOURCES/pg_idkit_13;      cp -r ~/pg_idkit/target/release/pg_idkit-pg13 ~/rpmbuild/SOURCES/pg_idkit_13;
rm -rf ~/rpmbuild/SOURCES/pg_idkit_12;      cp -r ~/pg_idkit/target/release/pg_idkit-pg12 ~/rpmbuild/SOURCES/pg_idkit_12;

rm -rf ~/rpmbuild/SOURCES/pgsmcrypto_16;    cp -r ~/pgsmcrypto/target/release/pgsmcrypto-pg16 ~/rpmbuild/SOURCES/pgsmcrypto_16;
rm -rf ~/rpmbuild/SOURCES/pgsmcrypto_15;    cp -r ~/pgsmcrypto/target/release/pgsmcrypto-pg15 ~/rpmbuild/SOURCES/pgsmcrypto_15;
rm -rf ~/rpmbuild/SOURCES/pgsmcrypto_14;    cp -r ~/pgsmcrypto/target/release/pgsmcrypto-pg14 ~/rpmbuild/SOURCES/pgsmcrypto_14;
rm -rf ~/rpmbuild/SOURCES/pgsmcrypto_13;    cp -r ~/pgsmcrypto/target/release/pgsmcrypto-pg13 ~/rpmbuild/SOURCES/pgsmcrypto_13;
rm -rf ~/rpmbuild/SOURCES/pgsmcrypto_12;    cp -r ~/pgsmcrypto/target/release/pgsmcrypto-pg12 ~/rpmbuild/SOURCES/pgsmcrypto_12;

rm -rf ~/rpmbuild/SOURCES/plprql_16;        cp -r ~/plprql/target/release/plprql-pg16 ~/rpmbuild/SOURCES/plprql_16;
rm -rf ~/rpmbuild/SOURCES/plprql_15;        cp -r ~/plprql/target/release/plprql-pg15 ~/rpmbuild/SOURCES/plprql_15;
rm -rf ~/rpmbuild/SOURCES/plprql_14;        cp -r ~/plprql/target/release/plprql-pg14 ~/rpmbuild/SOURCES/plprql_14;
rm -rf ~/rpmbuild/SOURCES/plprql_13;        cp -r ~/plprql/target/release/plprql-pg13 ~/rpmbuild/SOURCES/plprql_13;
rm -rf ~/rpmbuild/SOURCES/plprql_12;        cp -r ~/plprql/target/release/plprql-pg12 ~/rpmbuild/SOURCES/plprql_12;

rm -rf ~/rpmbuild/SOURCES/vectorscale_16; cp -r ~/pgvectorscale/pgvectorscale/target/release/vectorscale-pg16 ~/rpmbuild/SOURCES/vectorscale_16;
rm -rf ~/rpmbuild/SOURCES/vectorscale_15; cp -r ~/pgvectorscale/pgvectorscale/target/release/vectorscale-pg15 ~/rpmbuild/SOURCES/vectorscale_15;

rm -rf ~/rpmbuild/SOURCES/pgdd_16;          cp -r ~/pgdd/target/release/pgdd-pg16 ~/rpmbuild/SOURCES/pgdd_16;
rm -rf ~/rpmbuild/SOURCES/pgdd_15;          cp -r ~/pgdd/target/release/pgdd-pg15 ~/rpmbuild/SOURCES/pgdd_15;
rm -rf ~/rpmbuild/SOURCES/pgdd_14;          cp -r ~/pgdd/target/release/pgdd-pg14 ~/rpmbuild/SOURCES/pgdd_14;
rm -rf ~/rpmbuild/SOURCES/pgdd_13;          cp -r ~/pgdd/target/release/pgdd-pg13 ~/rpmbuild/SOURCES/pgdd_13;
rm -rf ~/rpmbuild/SOURCES/pgdd_12;          cp -r ~/pgdd/target/release/pgdd-pg12 ~/rpmbuild/SOURCES/pgdd_12;

rm -rf ~/rpmbuild/SOURCES/pg_tiktoken_16;   cp -r ~/pg_tiktoken/target/release/pg_tiktoken-pg16 ~/rpmbuild/SOURCES/pg_tiktoken_16;
rm -rf ~/rpmbuild/SOURCES/pg_tiktoken_15;   cp -r ~/pg_tiktoken/target/release/pg_tiktoken-pg15 ~/rpmbuild/SOURCES/pg_tiktoken_15;
rm -rf ~/rpmbuild/SOURCES/pg_tiktoken_14;   cp -r ~/pg_tiktoken/target/release/pg_tiktoken-pg14 ~/rpmbuild/SOURCES/pg_tiktoken_14;
rm -rf ~/rpmbuild/SOURCES/pg_tiktoken_13;   cp -r ~/pg_tiktoken/target/release/pg_tiktoken-pg13 ~/rpmbuild/SOURCES/pg_tiktoken_13;
rm -rf ~/rpmbuild/SOURCES/pg_tiktoken_12;   cp -r ~/pg_tiktoken/target/release/pg_tiktoken-pg12 ~/rpmbuild/SOURCES/pg_tiktoken_12;

cd ~/rpmbuild/SPECS
make pgml
make pg_search pg_lakehouse
make pg_graphql pg_jsonschema wrappers
make pgmq pg_later pg_vectorize pg_tier 
make pg_idkit pgsmcrypto plprql pgvectorscale
make pgdd pg_tiktoken
```




Example: build paradedb extensions

```bash
#---------------------------------------------#
# pg_search [RUST]
#---------------------------------------------#
pg_search:
	rm -rf ~/rpmbuild/RPMS/x86_64/pg_search*.rpm;
	rpmbuild --without debuginfo --define "pgmajorversion 16" -ba ~/rpmbuild/SPECS/pg_search.spec
	rpmbuild --without debuginfo --define "pgmajorversion 15" -ba ~/rpmbuild/SPECS/pg_search.spec

#---------------------------------------------#
# pg_lakehouse [RUST]
#---------------------------------------------#
pg_lakehouse:
	rm -rf ~/rpmbuild/RPMS/x86_64/pg_lakehouse*.rpm;
	rpmbuild --without debuginfo --define "pgmajorversion 16" -ba ~/rpmbuild/SPECS/pg_lakehouse.spec
	rpmbuild --without debuginfo --define "pgmajorversion 15" -ba ~/rpmbuild/SPECS/pg_lakehouse.spec
```




----------------

## Building `pgml`

The latest version of `pgml` is `v2.9.1`, which is compatible with `pg14`, `pg15` and `pg16`.

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

