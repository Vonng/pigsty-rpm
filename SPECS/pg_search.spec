%define debug_package %{nil}
%global pname pg_search
%global sname pg_search
%global pginstdir /usr/pgsql-%{pgmajorversion}

Name:		%{sname}_%{pgmajorversion}
Version:	0.7.0
Release:	1PIGSTY%{?dist}
Summary:	Full text search over SQL tables using the BM25 algorithm
License:	GNU Affero General Public License v3.0
URL:		https://github.com/paradedb/paradedb/tree/dev/%{sname}

BuildRequires:	postgresql%{pgmajorversion}-devel pgdg-srpm-macros >= 1.0.27
Requires:	postgresql%{pgmajorversion}-server

%description
pg_search is a PostgreSQL extension that enables full text search over SQL tables using the BM25 algorithm,
the state-of-the-art ranking function for full text search.
It is built on top of Tantivy, the Rust-based alternative to Apache Lucene, using pgrx.

%install
%{__rm} -rf %{buildroot}
install -d %{buildroot}%{pginstdir}/lib/
install -d %{buildroot}%{pginstdir}/share/extension/
install -m 755 %{_sourcedir}/pg_search_%{pgmajorversion}/usr/pgsql-%{pgmajorversion}/lib/pg_search.so %{buildroot}%{pginstdir}/lib/
install -m 644 %{_sourcedir}/pg_search_%{pgmajorversion}/usr/pgsql-%{pgmajorversion}/share/extension/pg_search*.sql %{buildroot}%{pginstdir}/share/extension/
install -m 644 %{_sourcedir}/pg_search_%{pgmajorversion}/usr/pgsql-%{pgmajorversion}/share/extension/pg_search.control %{buildroot}%{pginstdir}/share/extension/

%files
%{pginstdir}/lib/%{pname}.so
%{pginstdir}/share/extension/%{pname}.control
%{pginstdir}/share/extension/%{pname}*sql
%exclude /usr/lib/.build-id

%changelog
* Sat May 15 2024 Vonng <rh@vonng.com> - 0.7.0
* Sat Apr 27 2024 Vonng <rh@vonng.com> - 0.6.1
* Sat Feb 17 2024 Vonng <rh@vonng.com> - 0.5.6
* Mon Jan 29 2024 Vonng <rh@vonng.com> - 0.5.3
- Initial RPM release, used by Pigsty <https://pigsty.io>