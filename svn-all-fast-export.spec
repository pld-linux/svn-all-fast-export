Summary:	A fast-import based converter for an svn repo to git repos
Name:		svn-all-fast-export
Version:	1.0.10
Release:	1
License:	GPL v3
Group:		Development/Tools
Source0:	https://github.com/svn-all-fast-export/svn2git/archive/%{version}.tar.gz
# Source0-md5:	c94acdfb6eeb210fb8654436d179d946
Patch0:		git.patch
URL:		https://github.com/svn-all-fast-export/svn2git
BuildRequires:	apr-devel
BuildRequires:	qt4-qmake >= 4.3.3-3
BuildRequires:	rpmbuild(macros) >= 1.484
BuildRequires:	subversion-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
svn-all-fast-export is a tool to convert your svn repositories to git.

You will need to have a copy of your svn repository and to write some
rules to specify how the conversion will be done, for instance, you
can manage how the tags and branches will be managed writing the
appropriate rules. You have examples in
%{_examplesdir}/%{name}-%{version}

Also, you can provide a file mapping the old svn accounts to the
authors names in the format "Author Name <email>" so will not need to
use git filter-branch to amend the commiters' names.

#'<- for vim

%prep
%setup -qc
mv svn2git-*/* .
%patch0 -p1

%build
cd src

cat > local-config.pri <<EOF
APR_INCLUDE = $(apr-1-config --includedir)
EOF

qmake-qt4
%{__make} \
	CXX="%{__cxx}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_examplesdir}/%{name}-%{version}}
install -p svn-all-fast-export $RPM_BUILD_ROOT%{_bindir}
cp -a samples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/svn-all-fast-export
%{_examplesdir}/%{name}-%{version}
