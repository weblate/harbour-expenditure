# 
# Do NOT Edit the Auto-generated Part!
# Generated by: spectacle version 0.32
# 

Name:       harbour-expenditure

# >> macros
# << macros
%define __provides_exclude_from ^%{_datadir}/.*$

Summary:    Expenditure
Version:    1.1.0
Release:    1
Group:      Applications/Productivity
License:    GPL-3.0-or-later
URL:        https://github.com/ichthyosaurus/harbour-expenditure
Source0:    %{name}-%{version}.tar.bz2
Source100:  harbour-expenditure.yaml
Requires:   sailfishsilica-qt5 >= 0.10.9
Requires:   pyotherside-qml-plugin-python3-qt5 >= 1.5.0
BuildRequires:  pkgconfig(sailfishapp) >= 1.0.2
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5Qml)
BuildRequires:  pkgconfig(Qt5Quick)
BuildRequires:  desktop-file-utils

%description
A simple app for tracking expenses in groups.

%if 0%{?_chum}
Title: Expenditure
Type: desktop-application
DeveloperName: ichthyosaurus
Categories:
- Office
Custom:
  Repo: https://github.com/ichthyosaurus/harbour-expenditure
PackageIcon: https://github.com/ichthyosaurus/harbour-expenditure/raw/main/icons/172x172/harbour-expenditure.png
Screenshots:
- https://github.com/ichthyosaurus/harbour-expenditure/raw/main/dist/screenshots-openrepos/screenshot-01.jpg
- https://github.com/ichthyosaurus/harbour-expenditure/raw/main/dist/screenshots-openrepos/screenshot-02.jpg
- https://github.com/ichthyosaurus/harbour-expenditure/raw/main/dist/screenshots-openrepos/screenshot-03.jpg
- https://github.com/ichthyosaurus/harbour-expenditure/raw/main/dist/screenshots-openrepos/screenshot-04.jpg
Links:
  Homepage: https://github.com/ichthyosaurus/harbour-expenditure
  Help: https://forum.sailfishos.org/t/apps-by-ichthyosaurus/15753
  Bugtracker: https://github.com/ichthyosaurus/harbour-expenditure/issues
  Donation: https://liberapay.com/ichthyosaurus
%endif


%prep
%setup -q -n %{name}-%{version}

# >> setup
# << setup

%build
# >> build pre
# << build pre

%qmake5  \
    VERSION=%{version} \
    RELEASE=%{release}

make %{?_smp_mflags}

# >> build post
# << build post

%install
rm -rf %{buildroot}
# >> install pre
# << install pre
%qmake5_install

# >> install post
# << install post

desktop-file-install --delete-original       \
  --dir %{buildroot}%{_datadir}/applications             \
   %{buildroot}%{_datadir}/applications/*.desktop

%files
%defattr(-,root,root,-)
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.png
# >> files
# << files
