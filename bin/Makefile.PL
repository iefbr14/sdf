
use ExtUtils::MakeMaker;

WriteMakefile(
	NAME		=> 'SDF::bin',

	EXE_FILES	=> [ qw(
mkpldocs
pod2sdf
poddiff
sdf
sdfapi
sdfcli
sdfget
			) ],
	);

