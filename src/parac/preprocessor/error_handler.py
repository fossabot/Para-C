# coding=utf-8
""" Error handler for the preprocessor parser and lexer """
import logging
from typing import Union
from antlr4.error.Errors import (InputMismatchException,
                                 FailedPredicateException,
                                 RecognitionException,
                                 LexerNoViableAltException,
                                 NoViableAltException)

from ..abc import BaseErrorListener

__all__ = [
    'PreProcessorErrorListener',
]

logger = logging.getLogger(__name__)


class PreProcessorErrorListener(BaseErrorListener):
    """ Error-Listener for the PreProcessor """

    def __init__(self, reraise: bool):
        """
        Initialises the instance

        :param reraise: If set to True the error listener will reraise errors
        and not just log them
        """
        super().__init__(reraise)

    def reportAmbiguity(
            self,
            recognizer,
            dfa,
            startIndex,
            stopIndex,
            exact,
            ambigAlts,
            configs
    ) -> None:
        """
        This method is called by the parser when a full-context prediction
        results in an ambiguity.
        """
        ...

    def reportAttemptingFullContext(
            self,
            recognizer,
            dfa,
            startIndex,
            stopIndex,
            conflictingAlts,
            configs
    ) -> None:
        """
        This method is called when an SLL conflict occurs and the parser is
        about to use the full context information to make an LL decision.
        """
        ...

    def reportContextSensitivity(
            self,
            recognizer,
            dfa,
            startIndex,
            stopIndex,
            prediction,
            configs
    ) -> None:
        """
        This method is called by the parser when a full-context prediction
        has a unique result.
        """
        ...

    def syntaxError(
            self,
            recognizer,
            offendingSymbol,
            line: int,
            column: int,
            msg: str,
            e: Union[
                RecognitionException,
                NoViableAltException,
                LexerNoViableAltException,
                InputMismatchException,
                FailedPredicateException
            ]
    ) -> None:
        """
        Method which will be called if the ANTLR4 Lexer or Parser detect
        an error inside the program
        """
        # TODO! Add proper error handling
        logger.error(f"At line: {line}, column: {column} - {msg}")
