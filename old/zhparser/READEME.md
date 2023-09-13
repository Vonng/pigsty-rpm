# Zhparser



---------

## 从 SRPM 构建 zhparser

```bash

#============================================
# Prepare
#============================================
# write pgdg srpm repo
cat > /etc/yum.repos.d/pgdg15-srpm.repo <<-'EOF'
[pgdg15-srpm]
name = PostgreSQL 15 SRPM $releasever - $basearch
baseurl=https://mirrors.tuna.tsinghua.edu.cn/postgresql/repos/yum/srpms/common/redhat/rhel-$releasever-x86_64/
gpgcheck = 0
enabled = 1
module_hotfixes=1
EOF

# install deps
yum install -y pgdg-srpm-macros
yum install -y clang ccache # el9 optional
yum install -y rpm-build rpmdevtools
rpmdev-setuptree;


#============================================
# SCWS
#============================================
# download srpm
rpm -ivh https://get.pigsty.cc/yum/srpm/scws-1.2.3-PIGSTY1.src.rpm

# generate rpm
QA_RPATHS=$[ 0x0002 ] rpmbuild -ba ~/rpmbuild/SPECS/scws.spec

# copy rpm to /tmp/scws
rm -rf /tmp/scws; mkdir -p /tmp/scws; mv -f  ~/rpmbuild/RPMS/x86_64/scws-* /tmp/scws/

# install scws for zhparser
rpm -ivh /tmp/scws/scws-1.2.3-PIGSTY1.el*.x86_64.rpm

#============================================
# ZHPARSER
#============================================
# install zhparser srpm
rpm -ivh https://get.pigsty.cc/yum/srpm/zhparser-2.2-PIGSTY1.src.rpm

rpmbuild --define "pgmajorversion 15" -ba ~/rpmbuild/SPECS/zhparser.spec;
rpmbuild --define "pgmajorversion 14" -ba ~/rpmbuild/SPECS/zhparser.spec;
rpmbuild --define "pgmajorversion 13" -ba ~/rpmbuild/SPECS/zhparser.spec;
rpmbuild --define "pgmajorversion 12" -ba ~/rpmbuild/SPECS/zhparser.spec;
rpmbuild --define "pgmajorversion 16" -ba ~/rpmbuild/SPECS/zhparser.spec;

# copy to /tmp/zhparser
rm -rf /tmp/zhparser; mkdir -p /tmp/zhparser; mv -f  ~/rpmbuild/RPMS/x86_64/zhparse* /tmp/zhparser/
```


```bash
# copy to pigsty
cp -r /tmp/scws/scws*rpm         /www/pigsty;
cp -r /tmp/zhparser/zhparser*rpm /www/pigsty;
```



---------

## SCWS RPM制作

```bash
yum install -y rpm-build rpmdevtools
rpmdev-setuptree;

# 下载源代码
curl http://www.xunsearch.com/scws/down/scws-1.2.3.tar.bz2 -o ~/rpmbuild/SOURCES/scws-1.2.3.tar.bz2

# 生成 SPEC 文件
cat > ~/rpmbuild/SPECS/scws.spec <<-'EOF'
Name:           scws
Version:        1.2.3
Release:        PIGSTY1%{?dist}
Summary:        Simple Chinese Word Segmentation

License:        BSD
URL:            http://www.xunsearch.com/scws/
Source0:        http://www.xunsearch.com/scws/down/%{name}-%{version}.tar.bz2

BuildRequires:  gcc, make
Requires:       glibc

%description
SCWS (Simple Chinese Word Segmentation) is a high performance Chinese word segmentation utility.
https://github.com/hightman/scws/blob/master/COPYING
build with QA_RPATHS=$[ 0x0002 ] rpmbuild -ba ~/rpmbuild/SPECS/scws.spec

%prep
%setup -q

%build
LDFLAGS="-Wl,--disable-new-dtags" ./configure
make

%install
make install DESTDIR=%{buildroot}

%files
/usr/local/bin/scws
/usr/local/bin/scws-gen-dict
/usr/local/lib/libscws.*
/usr/local/include/scws/*
/usr/local/etc/rules.ini
/usr/local/etc/rules.utf8.ini
/usr/local/etc/rules_cht.utf8.ini
%exclude /usr/lib/.build-id/*

%post
/sbin/ldconfig

%postun
/sbin/ldconfig

%changelog
* Wed Sep 13 2023 Vonng <rh@vonng.com> - 1.2.3-1
- Initial RPM release

EOF

# 生成 SRPM
rpmbuild -bs ~/rpmbuild/SPECS/scws.spec

# 重命名 SRPM
mv -f ~/rpmbuild/SRPMS/scws-1.2.3-PIGSTY1.el*.src.rpm ~/rpmbuild/SRPMS/scws-1.2.3-PIGSTY1.src.rpm
ls ~/rpmbuild/SRPMS/scws-1.2.3-PIGSTY1.src.rpm

# 从 SRPM 开始编译生成 RPM
QA_RPATHS=$[ 0x0002 ] rpmbuild --rebuild ~/rpmbuild/SRPMS/scws-1.2.3-PIGSTY1.src.rpm

# 拷贝产出 至 /tmp/scws
rm -rf /tmp/scws; mkdir -p /tmp/scws; mv -f  ~/rpmbuild/RPMS/x86_64/scws-* /tmp/scws/

# 装箱放入 /www/pigsty
cp -r /tmp/scws/scws*rpm /www/pigsty
```



---------

## zhparser RPM制作

```bash
# 安装 scws
rpm -ivh /tmp/scws/scws-1.2.3-1.el*.x86_64.rpm

# 安装 RPM macros
cat > /etc/yum.repos.d/pgdg15-srpm.repo <<-'EOF'
[pgdg15-srpm]
name = PostgreSQL 15 SRPM $releasever - $basearch
baseurl=https://mirrors.tuna.tsinghua.edu.cn/postgresql/repos/yum/srpms/common/redhat/rhel-$releasever-x86_64/
gpgcheck = 0
enabled = 1
module_hotfixes=1
EOF

yum install -y pgdg-srpm-macros
yum install -y clang ccache


# 下载源代码
curl https://github.com/amutu/zhparser/archive/refs/tags/V2.2.tar.gz -o ~/rpmbuild/SOURCES/V2.2.tar.gz

# 生成 SPEC 文件
cat > ~/rpmbuild/SPECS/zhparser.spec <<-'EOF'
%global pname zhparser
%global pginstdir /usr/pgsql-%{pgmajorversion}

Name:		%{pname}_%{pgmajorversion}
Version:	2.2
Release:	PIGSTY1%{?dist}
Summary:	Open-source full-text search of Chinese language
License:	PostgreSQL
URL:		https://github.com/amutu/zhparser/
Source0:	https://github.com/amutu/zhparser/archive/refs/tags/V2.2.tar.gz

BuildRequires:	postgresql%{pgmajorversion}-devel pgdg-srpm-macros >= 1.0.27
Requires:	postgresql%{pgmajorversion}-server scws

%description
zhparser is a PostgreSQL extension for full-text search of Chinese language (Mandarin Chinese).
It implements a Chinese language parser base on the Simple Chinese Word Segmentation(SCWS).

%prep
%setup -q -n %{pname}-%{version}

%build
PATH=%{pginstdir}/bin:$PATH %{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
PATH=%{pginstdir}/bin:$PATH %{__make} %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
%doc README.md
%{pginstdir}/lib/%{pname}.so
%{pginstdir}/share/extension/%{pname}.control
%{pginstdir}/share/extension/%{pname}*sql
%{pginstdir}/share/tsearch_data/dict.utf8.xdb
%{pginstdir}/share/tsearch_data/rules.utf8.ini
%exclude /usr/lib/.build-id/*
%exclude %{pginstdir}/lib/bitcode/zhparser*

%changelog
* Wed Sep 13 2023 Vonng <rh@vonng.com> - 2.2-1
- Initial RPM release

EOF

# 生成 SRPM
rm -rf ~/rpmbuild/SRPMS/zhparser_15-2.2.*.rpm
rpmbuild --define "pgmajorversion 15" -bs ~/rpmbuild/SPECS/zhparser.spec
#rpmbuild --define "pgmajorversion 15" -ba ~/rpmbuild/SPECS/zhparser.spec

# 重命名 SRPM
mv -f  ~/rpmbuild/SRPMS/zhparser_15-2.2-PIGSTY1.el*.src.rpm  ~/rpmbuild/SRPMS/zhparser_15-2.2-PIGSTY1.src.rpm
ls ~/rpmbuild/SRPMS/zhparser_15-2.2-PIGSTY1.src.rpm
cp ~/rpmbuild/SRPMS/zhparser_15-2.2-PIGSTY1.src.rpm /tmp/

# 从 SRPM 开始编译生成 RPM
rpmbuild --define "pgmajorversion 15"  --rebuild ~/rpmbuild/SRPMS/zhparser_15-2.2-PIGSTY1.src.rpm

# 拷贝产出 至 /tmp/zhparser
rm -rf /tmp/zhparser; mkdir -p /tmp/zhparser; mv -f  ~/rpmbuild/RPMS/x86_64/zhparse* /tmp/zhparser/

# 装箱放入 /www/pigsty
cp -r /tmp/zhparser/zhparser*rpm /www/pigsty
```



