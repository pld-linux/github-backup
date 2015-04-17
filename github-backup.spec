Summary:	backs up everything github knows about a repository, to the repository
Name:		github-backup
Version:	1.20150106
Release:	0.1
License:	GPL v3
Group:		Development/Languages
Source0:	https://github.com/joeyh/github-backup/archive/%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	b278a9b09243efc66638bf74554480d4
URL:		https://github.com/joeyh/github-backup
BuildRequires:	ghc >= 6.12.3
BuildRequires:	rpmbuild(macros) >= 1.608
%requires_releq	ghc
Requires(post,postun):	/usr/bin/ghc-pkg
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# debuginfo is not useful for ghc
%define		_enable_debug_packages	0

# don't compress haddock files
%define		_noautocompressdoc	*.haddock

%description
github-backup is a simple tool you run in a git repository you cloned
from GitHub. It backs up everything GitHub publishes about the
repository, including branches, tags, other forks, issues, comments,
wikis, milestones, pull requests, watchers, and stars.

Also includes gitriddance, which can be used to close all open issues
and pull requests.

%prep
%setup -q

%build

%install
rm -rf $RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.md
