# coding=utf-8
""" Logic Tree Listener for the Para-C Pre-Processor """
import logging
from typing import List
import antlr4
import logging

from .abc import PreProcessorLogicToken
from .python import ParaCPreProcessorListener
from .ctx import FilePreProcessorContext
from .python import ParaCPreProcessorParser as parser

__all__ = [
    'Listener'
]

logger = logging.getLogger(__name__)
_p = parser.ParaCPreProcessorParser


class Listener(ParaCPreProcessorListener.ParaCPreProcessorListener):
    """
    Listener that listens for events inside the parsing. It will inherit all
    generated methods from the ParaCPreProcessorListener and then define the
    wanted behaviour inside the preprocessor processing.
    """

    def __init__(
            self,
            antlr4_file_ctx: _p.CompilationUnitContext,
            file_stream: antlr4.InputStream,
            relative_file_name: str
    ):
        self._file_ctx = FilePreProcessorContext(relative_file_name)
        self.antlr4_file_ctx: _p.CompilationUnitContext = antlr4_file_ctx
        self.file_stream: antlr4.InputStream = file_stream
        self._enable_out = False

    @property
    def logic_stream(self) -> List[PreProcessorLogicToken]:
        """ Stream which stores the logical tokens for the passed file. """
        return self._file_ctx.logic_stream

    @property
    def file_ctx(self) -> FilePreProcessorContext:
        """ The file context for this class """
        return self._file_ctx

    async def walk_and_process_directives(self, enable_out: bool) -> None:
        """
        Walks through the passed compilation unit context and processes it.
        The file_ctx will be populated and able to be used for finishing
        the preprocessor processing steps

        :param enable_out: If set to True errors, warnings and info will be
        logged onto the console using the local logger instance. If an
        exception is raised or error is encountered, it will be reraised with
        the FailedToProcessError.
        """
        logger.debug(
            "Walking through the logic tree and generating logic stream"
        )
        self._enable_out = enable_out

    def enterCompilationUnit(
            self,
            ctx: _p.CompilationUnitContext
    ):
        """
        Enter a parse tree produced by parser#compilationUnit.
        """
        ...

    def exitCompilationUnit(
            self,
            ctx: _p.CompilationUnitContext
    ):
        """
        Exit a parse tree produced by parser#compilationUnit.
        """
        ...

    def enterTranslationUnit(
            self,
            ctx: _p.TranslationUnitContext
    ):
        """
        Enter a parse tree produced by parser#translationUnit.
        """
        ...

    def exitTranslationUnit(
            self,
            ctx: _p.TranslationUnitContext
    ):
        """
        Exit a parse tree produced by parser#translationUnit.
        """
        ...

    def enterExternalItem(
            self,
            ctx: _p.ExternalItemContext
    ):
        """
        Enter a parse tree produced by parser#externalItem.
        """
        ...

    def exitExternalItem(
            self,
            ctx: _p.ExternalItemContext
    ):
        """
        Exit a parse tree produced by parser#externalItem.
        """
        ...

    def enterPreProcessorDirective(
            self,
            ctx: _p.PreProcessorDirectiveContext
    ):
        """
        Enter a parse tree produced by parser#preProcessorDirective.
        """
        ...

    def exitPreProcessorDirective(
            self,
            ctx: _p.PreProcessorDirectiveContext
    ):
        """
        Exit a parse tree produced by parser#preProcessorDirective.
        """
        ...

    def enterSelectionPreProcessorDirective(
            self,
            ctx: _p.SelectionPreProcessorDirectiveContext
    ):
        """
        Enter a parse tree produced by parser#selectionPreProcessorDirective.
        """
        ...

    def exitSelectionPreProcessorDirective(
            self,
            ctx: _p.SelectionPreProcessorDirectiveContext
    ):
        """
        Exit a parse tree produced by parser#selectionPreProcessorDirective.
        """
        ...

    def enterStartOfSelectionBlock(
            self,
            ctx: _p.StartOfSelectionBlockContext
    ):
        """
        Enter a parse tree produced by parser#startSelectionBlock.
        """
        ...

    def exitStartOfSelectionBlock(
            self,
            ctx: _p.StartOfSelectionBlockContext
    ):
        """
        Exit a parse tree produced by parser#startSelectionBlock.
        """
        ...

    def enterSelectionDirectiveAlternatives(
            self,
            ctx: _p.SelectionDirectiveAlternativesContext
    ):
        """
        Enter a parse tree produced by parser#logicalDirectiveAlternatives.
        """
        ...

    def exitSelectionDirectiveAlternatives(
            self,
            ctx: _p.SelectionDirectiveAlternativesContext
    ):
        """
        Exit a parse tree produced by parser#logicalDirectiveAlternatives.
        """
        ...

    def enterSelectionElseDirective(
            self,
            ctx: _p.SelectionElseDirectiveContext
    ):
        """
        Enter a parse tree produced by parser#logicalElseDirective.
        """
        ...

    def exitSelectionElseDirective(
            self,
            ctx: _p.SelectionElseDirectiveContext
    ):
        """
        Exit a parse tree produced by parser#logicalElseDirective.
        """
        ...

    def enterErrorDirective(
            self,
            ctx: _p.ErrorDirectiveContext):
        """
        Enter a parse tree produced by ParaCPreProcessorParser#errorDirective.
        """
        ...

    def exitErrorDirective(
            self,
            ctx: _p.ErrorDirectiveContext):
        """
        Exit a parse tree produced by ParaCPreProcessorParser#errorDirective.
        """
        ...

    def enterLineDirective(
            self,
            ctx: _p.LineDirectiveContext):
        """
        Enter a parse tree produced by ParaCPreProcessorParser#lineDirective.
        """
        ...

    def exitLineDirective(
            self,
            ctx: _p.LineDirectiveContext):
        """
        Exit a parse tree produced by ParaCPreProcessorParser#lineDirective.
        """
        ...

    def enterIncludeDirective(
            self,
            ctx: _p.IncludeDirectiveContext
    ):
        """
        Enter a parse tree produced by parser#includeDirective.
        """
        ...

    def exitIncludeDirective(
            self,
            ctx: _p.IncludeDirectiveContext
    ):
        """
        Exit a parse tree produced by parser#includeDirective.
        """
        ...

    def enterFileIncludeDirective(
            self,
            ctx: _p.FileIncludeDirectiveContext
    ):
        """
        Enter a parse tree produced by parser#fileIncludeDirective.
        """
        ...

    def exitFileIncludeDirective(
            self,
            ctx: _p.FileIncludeDirectiveContext
    ):
        """
        Exit a parse tree produced by parser#fileIncludeDirective.
        """
        ...

    def enterComputedIncludeDirective(
            self,
            ctx: _p.ComputedIncludeDirectiveContext
    ):
        """
        Enter a parse tree produced by parser#computedIncludeDirective.
        """
        ...

    def exitComputedIncludeDirective(
            self,
            ctx: _p.ComputedIncludeDirectiveContext
    ):
        """
        Exit a parse tree produced by parser#computedIncludeDirective.
        """
        ...

    def enterComplexDefineDirective(
            self,
            ctx: _p.ComplexDefineDirectiveContext
    ):
        """
        Enter a parse tree produced by _p#complexDefineDirective.
        """
        ...

    def exitComplexDefineDirective(
            self,
            ctx: _p.ComplexDefineDirectiveContext
    ):
        """
        Exit a parse tree produced by _p#complexDefineDirective.
        """
        ...

    def enterPragmaDirective(
            self,
            ctx: _p.PragmaDirectiveContext
    ):
        """
        Enter a parse tree produced by _p#pragmaDirective.
        """
        ...

    def exitPragmaDirective(
            self,
            ctx: _p.PragmaDirectiveContext
    ):
        """
        Exit a parse tree produced by _p#pragmaDirective.
        """
        ...

    def enterUndefDirective(
            self,
            ctx: _p.UndefDirectiveContext
    ):
        """
        Enter a parse tree produced by _p#undefDirective.
        """
        ...

    def exitUndefDirective(
            self,
            ctx: _p.UndefDirectiveContext
    ):
        """
        Exit a parse tree produced by _p#undefDirective.
        """
        ...

    def enterIfNotDefinedDirective(
            self,
            ctx: _p.IfNotDefinedDirectiveContext
    ):
        """
        Enter a parse tree produced by
         ParaCPreProcessorParser#ifNotDefinedDirective.
        """
        ...

    def exitIfNotDefinedDirective(
            self,
            ctx: _p.IfNotDefinedDirectiveContext
    ):
        """
        Exit a parse tree produced by
        ParaCPreProcessorParser#ifNotDefinedDirective.
        """
        ...

    #
    def enterIfDefinedDirective(
            self,
            ctx: _p.IfDefinedDirectiveContext
    ):
        """
        Enter a parse tree produced by
        ParaCPreProcessorParser#ifDefinedDirective.
        """
        ...

    def exitIfDefinedDirective(
            self,
            ctx: _p.IfDefinedDirectiveContext
    ):
        """
        Exit a parse tree produced by
        ParaCPreProcessorParser#ifDefinedDirective.
        """
        ...

    def enterElIfNotDefinedDirective(
            self,
            ctx: _p.ElIfNotDefinedDirectiveContext
    ):
        """
        Enter a parse tree produced by
         ParaCPreProcessorParser#elIfNotDefinedDirective.
        """
        ...

    def exitElIfNotDefinedDirective(
            self,
            ctx: _p.ElIfNotDefinedDirectiveContext
    ):
        """
        Exit a parse tree produced by
        ParaCPreProcessorParser#elIfNotDefinedDirective.
        """
        ...

    def enterElIfDefinedDirective(
            self,
            ctx: _p.ElIfDefinedDirectiveContext
    ):
        """
        Enter a parse tree produced by
        ParaCPreProcessorParser#elIfDefinedDirective.
        """
        ...

    def exitElIfDefinedDirective(
            self,
            ctx: _p.ElIfDefinedDirectiveContext
    ):
        """
        Exit a parse tree produced by
        ParaCPreProcessorParser#elIfDefinedDirective.
        """
        ...

    def enterIfDirective(
            self,
            ctx: _p.IfDirectiveContext
    ):
        """
        Enter a parse tree produced by ParaCPreProcessorParser#ifDirective.
        """
        ...

    def exitIfDirective(
            self,
            ctx: _p.IfDirectiveContext
    ):
        """
        Exit a parse tree produced by ParaCPreProcessorParser#ifDirective.
        """
        ...

    def enterElIfDirective(
            self,
            ctx: _p.ElIfDirectiveContext
    ):
        """
        Enter a parse tree produced by ParaCPreProcessorParser#elIfDirective.
        """
        ...

    def exitElIfDirective(
            self,
            ctx: _p.ElIfDirectiveContext
    ):
        """
        Exit a parse tree produced by ParaCPreProcessorParser#elIfDirective.
        """
        ...

    def enterElseDirective(
            self,
            ctx: _p.ElseDirectiveContext
    ):
        """
        Enter a parse tree produced by ParaCPreProcessorParser#elseDirective.
        """
        ...

    def exitElseDirective(
            self,
            ctx: _p.ElseDirectiveContext
    ):
        """
        Exit a parse tree produced by ParaCPreProcessorParser#elseDirective.
        """
        ...

    def enterEndIfDirective(
            self,
            ctx: _p.EndIfDirectiveContext
    ):
        """
        Enter a parse tree produced by ParaCPreProcessorParser#endIfDirective.
        """
        ...

    def exitEndIfDirective(
            self,
            ctx: _p.EndIfDirectiveContext
    ):
        """
        Exit a parse tree produced by ParaCPreProcessorParser#endIfDirective.
        """
        ...

    def enterLibIncludeDirective(
            self,
            ctx: _p.LibIncludeDirectiveContext
    ):
        """
        Enter a parse tree produced by
        ParaCPreProcessorParser#libIncludeDirective.
        """
        ...

    def exitLibIncludeDirective(
            self,
            ctx: _p.LibIncludeDirectiveContext
    ):
        """
        Exit a parse tree produced by
        ParaCPreProcessorParser#libIncludeDirective.
        """
        ...

    def enterStringIncludeDirective(
            self,
            ctx: _p.StringIncludeDirectiveContext
    ):
        """
        Enter a parse tree produced by
         ParaCPreProcessorParser#stringIncludeDirective.
        """
        ...

    #
    def exitStringIncludeDirective(
            self,
            ctx: _p.StringIncludeDirectiveContext
    ):
        """
        Exit a parse tree produced by
        ParaCPreProcessorParser#stringIncludeDirective.
        """
        ...

    def enterNonPreProcessorItem(
            self,
            ctx: _p.NonPreProcessorItemContext
    ):
        """
        Enter a parse tree produced by
        ParaCPreProcessorParser#nonPreProcessorItem.
        """
        ...

    def exitNonPreProcessorItem(
            self,
            ctx: _p.NonPreProcessorItemContext
    ):
        """
        Exit a parse tree produced by
        ParaCPreProcessorParser#nonPreProcessorItem.
        """
        ...

    def enterAnySequence(
            self,
            ctx: _p.AnySequenceContext
    ):
        """
        Enter a parse tree produced by ParaCPreProcessorParser#anySequence.
        """
        ...

    def exitAnySequence(
            self,
            ctx: _p.AnySequenceContext
    ):
        """
        Exit a parse tree produced by ParaCPreProcessorParser#anySequence.
        """
        ...

    def enterPreProcessorEnd(
            self,
            ctx: _p.PreProcessorEndContext
    ):
        """
        Enter a parse tree produced by ParaCPreProcessorParser#preProcessorEnd.
        """
        ...

    def exitPreProcessorEnd(
            self,
            ctx: _p.PreProcessorEndContext
    ):
        """
        Exit a parse tree produced by ParaCPreProcessorParser#preProcessorEnd.
        """
        ...
