# TODO: system libmodplug, timidity?
Summary:	An abstract soundfile decoder
Summary(pl.UTF-8):	Abstrakcyjny dekoder plików dźwiękowych
Name:		SDL2_sound
Version:	2.0.1
Release:	1
License:	Zlib
Group:		Libraries
#Source0Download: https://github.com/icculus/SDL_sound/releases
Source0:	https://github.com/icculus/SDL_sound/archive/v%{version}/SDL_sound-%{version}.tar.gz
# Source0-md5:	4917a87b45f7b940a68cd1b60881cabb
URL:		http://www.icculus.org/SDL_sound/
BuildRequires:	SDL2-devel >= 2.0
BuildRequires:	cmake >= 2.8.12
Requires:	SDL2 >= 2.0
Obsoletes:	SDL_sound-play < 2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
SDL_sound is a library that handles the decoding of several popular
sound file formats, such as .WAV and .MP3. It is meant to make the
programmer's sound playback tasks simpler. The programmer gives
SDL_sound a filename, or feeds it data directly from one of many
sources, and then reads the decoded waveform data back at her leisure.
If resource constraints are a concern, SDL_sound can process sound
data in programmer-specified blocks. Alternately, SDL_sound can decode
a whole sound file and hand back a single pointer to the whole
waveform. SDL_sound can also handle sample rate, audio format, and
channel conversion on-the-fly and behind-the-scenes, if the programmer
desires.

%description -l pl.UTF-8
SDL_sound to biblioteka obsługująca dekodowanie kilku popularnych
formatów plików dźwiękowych, takich jak .WAV lub .MP3. Jej celem
jest uproszczenie pracy programisty przy odtwarzaniu dźwięku.
Programista przekazuje SDL_sound nazwę pliku lub dostarcza dane
bezpośrednio z jednego z wielu źródeł, a następnie odczytuje strumień
zdekodowanych danych. Jeśli ograniczenia zasobów są istotne, SDL_sound
może obsługiwać dane dźwiękowe w podanych blokach. Alternatywnie,
SDL_sound może dekodować cały plik dźwiękowy i przekazywać z powrotem
pojedynczy wskaźnik do całości zdekodowanych danych. SDL_sound może
także obsługiwać w locie konwersję częstotliwości próbkowania, formatu
dźwięku i liczby kanałów.

%package play
Summary:	SDL_sound/physfs based music player
Summary(pl.UTF-8):	Odtwarzacz muzyki oparty na SDL_sound/physfs
Group:		Applications/Sound
Requires:	%{name} = %{version}-%{release}
Requires:	physfs >= 3

%description play
SDL_sound/physfs based music player.

%description play -l pl.UTF-8
Odtwarzacz muzyki oparty na SDL_sound/physfs.

%package devel
Summary:	Header files and more to develop SDL_sound applications
Summary(pl.UTF-8):	Pliki nagłówkowe do tworzenia aplikacji z użyciem SDL_sound
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	SDL2-devel >= 2.0

%description devel
Header files and more to develop SDL_sound applications.

%description devel -l pl.UTF-8
Pliki nagłówkowe do tworzenia aplikacji z użyciem SDL_sound.

%package static
Summary:	Static SDL_sound libraries
Summary(pl.UTF-8):	Statyczne biblioteki SDL_sound
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static SDL_sound libraries.

%description static -l pl.UTF-8
Statyczne biblioteki SDL_sound.

%prep
%setup -q -n SDL_sound-%{version}

%build
install -d build 
cd build
%cmake .. \
	-DSDLSOUND_DECODER_MIDI=ON

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc LICENSE.txt docs/{CHANGELOG,CREDITS,README}.txt
%attr(755,root,root) %{_bindir}/playsound
%attr(755,root,root) %{_libdir}/libSDL2_sound.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libSDL2_sound.so.2

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libSDL2_sound.so
%{_includedir}/SDL2/SDL_sound.h

%files static
%defattr(644,root,root,755)
%{_libdir}/libSDL2_sound.a
