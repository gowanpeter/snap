#from plain.models import Piece, Condition, PublicationLookup, publication_link_piece, ExhibitionLookup, exhibition_link_piece, Documentation, documentation_link_piece, GlazeLookup, glaze_link_piece, HeathLineLookup, heath_line_link_piece, Logo,logo_link_piece, MakerLookup, maker_link_piece, MaterialLookup, material_link_piece, MethodLookup, method_link_piece, SetCollection, setCollection_link_piece

from plain.models import Piece, GlazeLookup, glaze_link_piece, HeathLineLookup, heath_line_link_piece, MakerLookup, maker_link_piece, MaterialLookup, material_link_piece, MethodLookup, method_link_piece

from autofixture import generators, register, AutoFixture


class  PieceAutoFixture(AutoFixture):
    field_values = {
        'cataloguer': generators.ChoicesGenerator(
            values="Erminia Galdamez, Angila Weekly,  Milton Burnley,  Earle Hampshire,  Lael Warford,  Leilani Dennis,  Porsha Nodine,  Tammie Wert,  Tonie Schweinsberg,  Meryl Belville,  Latricia Landrum,  Margorie Galeano,  Josiah Torgrimson,  Kurt Picklesimer, Veola Callaham, Rolf Humphery,  Shari Carpenter , Belen Hott  ".split(',')
        )
    }
register(Piece, PieceAutoFixture)

class GlazeLookupAutoFixture(AutoFixture):
    field_values = {
        'glaze_name': generators.ChoicesGenerator(
            values="aqua,black,blue,fuchsia,gray,green,lime,maroon,navy, olive,orange,purple,red,silver,teal,white,yellow".split(',')
        )
    }

register(GlazeLookup, GlazeLookupAutoFixture)

class  HeathLineLookupAutoFixture(AutoFixture):
    field_values = {
        'heath_line_name': generators.ChoicesGenerator(
            values="Coupe, Rim, Chez Pannise, Alabama Chanin".split(',')
        )
    }

register(HeathLineLookup, HeathLineLookupAutoFixture)

class  MakerLookupAutoFixture(AutoFixture):
    field_values = {
        'maker_name': generators.ChoicesGenerator(
            values="Erminia Galdamez, Angila Weekly,  Milton Burnley,  Earle Hampshire,  Lael Warford,  Leilani Dennis,  Porsha Nodine,  Tammie Wert,  Tonie Schweinsberg,  Meryl Belville,  Latricia Landrum,  Margorie Galeano,  Josiah Torgrimson,  Kurt Picklesimer, Veola Callaham, Rolf Humphery,  Shari Carpenter , Belen Hott  ".split(',')
        )
    }

register(MakerLookup, MakerLookupAutoFixture)

class  MaterialLookupAutoFixture(AutoFixture):
    field_values = {
        'material_name': generators.ChoicesGenerator(
            values="Clay, Slip, Mixed materials".split(',')
        )
    }

register(MaterialLookup, MaterialLookupAutoFixture)


class  MethodLookupAutoFixture(AutoFixture):
    field_values = {
        'method_name': generators.ChoicesGenerator(
            values="Hand thrown, Hand built, Cast, Jiggered".split(',')
        )
    }

register(MethodLookup, MethodLookupAutoFixture)


class ExhibitionLookupAutoFixture(AutoFixture):
    field_values = {
        'exhibition_name':generators.ChoicesGenerator(
            values="Arbitrary Relevance: 15 Years of Progress, Decadent Chemistry: Edith Heath and the Avant Garde, The Politics of Extravaganza: A Juried Show of Change, Parsing Charm: The Ceramic Art of Dilettantism, The Politics of Possibilities: Constructing a Praxis of Sameness, Ravilious, Royal Academy Summer Exhibition".split(',')
        )
    }

register(ExhibitionLookup, ExhibitionLookupAutoFixture)


class DocumentationAutoFixture(AutoFixture):
    field_values = {
        'documentation_name': generators.ChoicesGenerator(
            values=annual report, charter, concept statement , dossier, Green Paper, invitation to tender, palimpsest, screed, wordle, vignette'.split(',')
        )
    }

register(Documentation, DocumentationAutoFixture)


class LogoAutoFixture(AutoFixture):
    field_values = {
        'Logo_name': generators.ChoicesGenerator(
            values="Stamped, Incised, Drawn".split(',')
        )
    }

register(Logo, LogoAutoFixture)


class PublicationLookupAutoFixture(AutoFixture):
    field_values = {
        'publication_name': generators.ChoicesGenerator(
            values="The Judicious Ceramicist, The Methodical Ceramicist, The Meticulous Ceramicist, The Punctilious Ceramicist, Ceramic News, The Ceramic Advisor, Ceramic Intelligence".split(',')
        )
    }

register(PublicationLookup, PublicationLookupAutoFixture)


class SetCollectionAutoFixture(AutoFixture):
    field_values = {
        'set_collection_name': generators.ChoicesGenerator(
            values="Peter MacStewart, Museum of Modern Art, Heath, ".split(',')
        )
    }

register(SetCollection, SetCollectionAutoFixture)


