% rules.pl - Inference Engine

:- consult('kb.pl').

% Find civilizations by region
civilization_by_region(Region, Name) :-
    civilization(Name),
    region(Name, Region).

% Find civilizations by writing system
civilization_by_writing(System, Name) :-
    civilization(Name),
    writing_system(Name, System).

% Solve an archaeological dig mystery using River + Writing system
identify_dig_site(River, Writing, Match) :-
    civilization(Match),
    river(Match, River),
    writing_system(Match, Writing).

% Get full dossier for a civilization
dossier(Civ, Region, River, Writing) :-
    civilization(Civ),
    region(Civ, Region),
    river(Civ, River),
    writing_system(Civ, Writing).