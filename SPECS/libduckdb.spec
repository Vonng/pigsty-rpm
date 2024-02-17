Name:           libduckdb
Version:        0.9.2
Release:        1PIGSTY%{?dist}
Summary:        In-process SQL OLAP Database Management System
License:        MIT License
URL:            https://github.com/duckdb/duckdb/
Source0:        libduckdb.so

# cd ~/rpmbuild/SOURCES
# curl -L https://github.com/duckdb/duckdb/releases/download/v0.9.2/libduckdb-linux-amd64.zip -o libduckdb-linux-amd64.zip
# unzip -d . libduckdb-linux-amd64.zip

%description
DuckDB is a high-performance analytical database system.
It is designed to be fast, reliable, portable, and easy to use.
DuckDB provides a rich SQL dialect, with support far beyond basic SQL.
DuckDB supports arbitrary and nested correlated subqueries, window functions,
collations, complex types (arrays, structs), and more.

%prep

%build

%install
mkdir -p %{buildroot}/usr/lib64
install -m 0755 %{SOURCE0} %{buildroot}/usr/lib64

%files
/usr/lib64/libduckdb.so

%post
/sbin/ldconfig

%postun
/sbin/ldconfig

%changelog
* Tue Jan 30 2024 Vonng <rh@vonng.com> - 0.9.2-1PIGSTY
- Initial RPM release, used by Pigsty <https://pigsty.cc>