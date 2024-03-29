%define debug_package %{nil}
%global pname pg_bm25
%global sname pg_bm25
%global pginstdir /usr/pgsql-%{pgmajorversion}

Name:		%{sname}_%{pgmajorversion}
Version:	0.5.6
Release:	1PIGSTY%{?dist}
Summary:	Full text search over SQL tables using the BM25 algorithm
License:	GNU Affero General Public License v3.0
URL:		https://github.com/paradedb/paradedb/tree/dev/%{sname}
#Source0:	https://github.com/supabase/%{sname}/archive/refs/tags/pg_bm25-0.5.6.tar.gz
#           https://github.com/supabase/pg_bm25/archive/refs/tags/v0.5.6.tar.gz

BuildRequires:	postgresql%{pgmajorversion}-devel pgdg-srpm-macros >= 1.0.27
Requires:	postgresql%{pgmajorversion}-server

%description
pg_bm25 is a PostgreSQL extension that enables full text search over SQL tables using the BM25 algorithm,
the state-of-the-art ranking function for full text search.
It is built on top of Tantivy, the Rust-based alternative to Apache Lucene, using pgrx.

%install
%{__rm} -rf %{buildroot}
install -d %{buildroot}%{pginstdir}/lib/
install -d %{buildroot}%{pginstdir}/share/extension/
install -m 755 %{_sourcedir}/pg_bm25_%{pgmajorversion}/usr/pgsql-%{pgmajorversion}/lib/pg_bm25.so %{buildroot}%{pginstdir}/lib/
install -m 644 %{_sourcedir}/pg_bm25_%{pgmajorversion}/usr/pgsql-%{pgmajorversion}/share/extension/pg_bm25*.sql %{buildroot}%{pginstdir}/share/extension/
install -m 644 %{_sourcedir}/pg_bm25_%{pgmajorversion}/usr/pgsql-%{pgmajorversion}/share/extension/pg_bm25.control %{buildroot}%{pginstdir}/share/extension/

%files
%{pginstdir}/lib/%{pname}.so
%{pginstdir}/share/extension/%{pname}.control
%{pginstdir}/share/extension/%{pname}*sql
%exclude /usr/lib/.build-id

%changelog
* Sat Feb 17 2024 Vonng <rh@vonng.com> - 0.5.6
* Mon Jan 29 2024 Vonng <rh@vonng.com> - 0.5.3
- Initial RPM release, used by Pigsty <https://pigsty.cc>