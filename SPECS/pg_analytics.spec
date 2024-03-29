%define debug_package %{nil}
%global pname pg_analytics
%global sname pg_analytics
%global pginstdir /usr/pgsql-%{pgmajorversion}

Name:		%{sname}_%{pgmajorversion}
Version:	0.5.6
Release:	1PIGSTY%{?dist}
Summary:	accelerates analytical query processing inside Postgres
License:	GNU Affero General Public License v3.0
URL:		https://github.com/paradedb/paradedb/tree/dev/%{sname}
#Source0:	https://github.com/supabase/%{sname}/archive/refs/tags/pg_analytics-0.5.6.tar.gz
#           https://github.com/supabase/pg_analytics/archive/refs/tags/v0.5.6.tar.gz

BuildRequires:	postgresql%{pgmajorversion}-devel pgdg-srpm-macros >= 1.0.27
Requires:	postgresql%{pgmajorversion}-server

%description
pg_analytics is an extension that accelerates analytical query processing inside Postgres.
The performance of analytical queries that leverage pg_analytics is comparable to the performance
of dedicated OLAP databases — without the need to extract, transform, and load (ETL) the data
from your Postgres instance into another system. The purpose of pg_analytics is to be a drop-in
solution for fast analytics in Postgres with zero ETL.

The primary dependencies are:
Apache Arrow for column-oriented memory format
Apache DataFusion for vectorized query execution with SIMD
Apache Parquet for persistence
Delta Lake as a storage framework with ACID properties
pgrx, the framework for creating Postgres extensions in Rust

%install
%{__rm} -rf %{buildroot}
install -d %{buildroot}%{pginstdir}/lib/
install -d %{buildroot}%{pginstdir}/share/extension/
install -m 755 %{_sourcedir}/pg_analytics_%{pgmajorversion}/usr/pgsql-%{pgmajorversion}/lib/pg_analytics.so %{buildroot}%{pginstdir}/lib/
install -m 644 %{_sourcedir}/pg_analytics_%{pgmajorversion}/usr/pgsql-%{pgmajorversion}/share/extension/pg_analytics*.sql %{buildroot}%{pginstdir}/share/extension/
install -m 644 %{_sourcedir}/pg_analytics_%{pgmajorversion}/usr/pgsql-%{pgmajorversion}/share/extension/pg_analytics.control %{buildroot}%{pginstdir}/share/extension/

%files
%{pginstdir}/lib/%{pname}.so
%{pginstdir}/share/extension/%{pname}.control
%{pginstdir}/share/extension/%{pname}*sql
%exclude /usr/lib/.build-id

%changelog
* Sat Feb 17 2024 Vonng <rh@vonng.com> - 0.5.6
* Mon Jan 29 2024 Vonng <rh@vonng.com> - 0.5.3
- Initial RPM release, used by Pigsty <https://pigsty.cc>