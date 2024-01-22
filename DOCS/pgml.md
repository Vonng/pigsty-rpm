# pgml

[Latest Guide](https://postgresml.org/docs/resources/developer-docs/installation) | [Old Guide](https://postgresml.org/docs/guides/setup/v2/installation)

Install rust & dependencies

```bash
cargo install cargo-pgrx --version 0.11.2
cargo pgrx init
```

```bash
sudo yum install -y openblas* python3.11 python3.11-devel lld

sudo yum install python3.11 python3.11-devel python3-virtualenv openssl openssl-devel cmake pkg-config libomp libomp-devel openblas* llvm llvm-devel
sudo alternatives --set python /usr/bin/python3.11 
```


EL 8.9 ad hoc logic

```bash
sudo dnf install devtoolset-9
source /opt/rh/gcc-toolset-9/enable
```

Change `build.rs`:

```bash
fn main() {
    #[cfg(target_os = "macos")]
    {
        println!("cargo:rustc-link-search=/opt/homebrew/opt/openblas/lib");
        println!("cargo:rustc-link-search=/opt/homebrew/opt/libomp/lib");
    }

    // PostgreSQL is using dlopen(RTLD_GLOBAL). this will parse some
    // of symbols into the previous opened .so file, but the others will use a
    // relative offset in pgml.so, and will cause a null-pointer crash.
    //
    // hide all symbol to avoid symbol conflicts.
    //
    // append mode (link-args) only works with clang ld (lld)
    println!(
        "cargo:link-args=-Wl,--version-script={}/ld.map",
        std::env::current_dir().unwrap().to_string_lossy(),
    );

    println!("cargo:rustc-link-lib=static=stdc++fs");
    println!("cargo:rustc-link-search=native=/opt/rh/gcc-toolset-9/root/usr/lib/gcc/x86_64-redhat-linux/9");

    vergen::EmitBuilder::builder().all_git().emit().unwrap();
}
```

Change `Cargo.toml`

```bash
[build-dependencies]
vergen = { version = "8", features = ["build", "git", "gitcl"] }
cc = "1.0"
```





Build for PG 14 / 15 / 16


```bash
git clone --recursive https://github.com/postgresml/postgresml.git
cd ~/postgresml/pgml-extension
export ALL_PROXY=http://192.168.0.104:8118
HTTPS_PROXY=http://192.168.0.104:8118 cargo pgrx install  --release -v
cargo pgrx package

export PATH=/usr/pgsql-16/bin:/root/.cargo/bin:/pg/bin:/usr/share/Modules/bin:/usr/lib64/ccache:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/root/bin:/home/vagrant/.cargo/bin
HTTPS_PROXY=http://192.168.0.104:8118 cargo pgrx package # build pg 16

export PATH=/usr/pgsql-15/bin:/root/.cargo/bin:/pg/bin:/usr/share/Modules/bin:/usr/lib64/ccache:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/root/bin:/home/vagrant/.cargo/bin
cargo pgrx package # build pg 15

export PATH=/usr/pgsql-14/bin:/root/.cargo/bin:/pg/bin:/usr/share/Modules/bin:/usr/lib64/ccache:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/root/bin:/home/vagrant/.cargo/bin
cargo pgrx package # build pg 14
```

Copying them into `rpmbuild/SOURCES`

```bash
rm -rf ~/rpmbuild/SOURCES/pgml_16; cp -r ~/postgresml/pgml-extension/target/release/pgml-pg16 ~/rpmbuild/SOURCES/pgml_16;
rm -rf ~/rpmbuild/SOURCES/pgml_15; cp -r ~/postgresml/pgml-extension/target/release/pgml-pg15 ~/rpmbuild/SOURCES/pgml_15;
rm -rf ~/rpmbuild/SOURCES/pgml_14; cp -r ~/postgresml/pgml-extension/target/release/pgml-pg14 ~/rpmbuild/SOURCES/pgml_14;
```

PGML Rpm

```bash
rpmbuild --without debuginfo --define "pgmajorversion 16" -ba ~/rpmbuild/SPECS/pgml.spec
rpmbuild --without debuginfo --define "pgmajorversion 15" -ba ~/rpmbuild/SPECS/pgml.spec
rpmbuild --without debuginfo --define "pgmajorversion 14" -ba ~/rpmbuild/SPECS/pgml.spec
```


```bash
# extract from previews rpm

rm -rf /root/rpmbuild/SOURCES/pgml_15
mkdir -p /root/rpmbuild/SOURCES/pgml_15
cd /root/rpmbuild/SOURCES/pgml_15;

rpm2cpio /www/pigsty/postgresml_15-2.8.1-PIGSTY1.el8.x86_64.rpm | cpio -idmv
rpm2cpio /www/pigsty/postgresml_15-2.8.1-PIGSTY1.el9.x86_64.rpm | cpio -idmv

rpmbuild --without debuginfo --define "pgmajorversion 16" -ba /root/rpmbuild/SPECS/pgml.spec
rpmbuild --without debuginfo --define "pgmajorversion 15" -ba /root/rpmbuild/SPECS/pgml.spec
rpmbuild --without debuginfo --define "pgmajorversion 14" -ba /root/rpmbuild/SPECS/pgml.spec

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







```bash
rpm2cpio /www/pigsty/p

```